from statistics_service import StatisticsService, SortBy
from player import Player
import unittest

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        reader = PlayerReaderStub()
        self.stats = StatisticsService(reader)

    def test_team(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertEqual(edm_players[0].name, "Semenko")
        self.assertEqual(edm_players[1].name, "Kurri")
        self.assertEqual(edm_players[2].name, "Gretzky")

        pit_players = self.stats.team("PIT")
        self.assertEqual(len(pit_players), 1)
        self.assertEqual(pit_players[0].name, "Lemieux")

        det_players = self.stats.team("DET")
        self.assertEqual(len(det_players), 1)
        self.assertEqual(det_players[0].name, "Yzerman")

    def test_top_by_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Kurri")

    def test_top_by_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Lemieux")

    def test_top(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        player_none = self.stats.search("Nonexistent")
        self.assertIsNone(player_none)


if __name__=="__main__":
    unittest.main()
