import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from unittest.mock import Mock, ANY
from src.kauppa import Kauppa
from src.viitegeneraattori import Viitegeneraattori
from src.varasto import Varasto
from src.tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        self.tuote1 = Tuote(1, "maito", 5)
        self.tuote2 = Tuote(2, "vesi", 3)
        self.tuote3 = Tuote(3, "loppu", 2)

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0
            

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return self.tuote1
            if tuote_id == 2:
                return self.tuote2
            if tuote_id == 3:
                return self.tuote3
            

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)    
                    
    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)      

    def test_kaksi_tuotetta_oikea_summa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)

        self.kauppa.tilimaksu("minttu", "100")

        self.pankki_mock.tilisiirto.assert_called_with("minttu", 42, "100", ANY, 5+3)

    def test_loppunut_tuote(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("loppu", "111")
        self.pankki_mock.tilisiirto.assert_called_with("loppu", 42, "111", ANY, 5)
    
    def test_aloitus(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("nollaus", "112")
        self.pankki_mock.tilisiirto.assert_called_with("nollaus", 42, "112", ANY, 3)


    def test_poista_korista(self):
        ostoskori_mock = Mock()
        self.kauppa._ostoskori = ostoskori_mock
        self.kauppa.poista_korista(1)
        self.varasto_mock.hae_tuote.assert_called_with(1)
        ostoskori_mock.poista.assert_called_with(self.tuote1)
        self.varasto_mock.palauta_varastoon.assert_called_with(self.tuote1)

#Muistelin et kaikki luokat piti testata, mut oli vääräs mut no tossa vielä nämä..
    def test_tuote_str(self):
        tuote_nimi = Tuote(4, "testi", 2)
        self.assertEqual(str(tuote_nimi), "testi")

    def test_tuote_eq(self):
        self.assertFalse(self.tuote1 == self.tuote2)
