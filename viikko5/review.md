Katselmoinnin suoritin ulkoisella copilotilla, koska minulla ei GitHubissa ole pro versiota, joten en saanut Copilottia sinne. Kuitenkin tässä muita huomioita Copilotilta:



Mitä huomioita Copilot teki koodistasi



* score\_when\_end\_game palauttaa ensin score-muuttujaan ja sitten lopuksi sen. Voisi palauttaa suoraan ilman välivaihetta.
* score\_normal käyttää suoraan listaa score\_names, mutta ei tarkista virhetilanteita (esim. jos pisteet > 3).
* get\_score voisi olla selkeämpi, jos logiikkaa yhdistetään. Nyt se delegoi kolmeen eri metodiin, mikä on hyvä, mutta hieman hajauttaa yksinkertaista logiikkaa.





Olivatko ehdotetut muutokset hyviä:

Mielestäni monet ehdotukset ovat ihan hyvia ja ihan oikeassa se on, että teen ylimääräisiä steppejä kun en palauta suoraan ilman välivaiheita. 



Kuinka hyödylliseksi koit Copilotin tekemän katselmoinnin:

En ole kauheen kokenut koodaaja vielä, niin monet virheet ja typot saattaa jäädä huomaamatta, joten koen ainakin tälläisten kannalta sen hyödylliseks ja yleiseti tässä sen logiikka on mielestäni parempi kuin minun.







Copilotin ehdottama versio:

class TennisGame:

&nbsp;   SCORE\_NAMES = \["Love", "Fifteen", "Thirty", "Forty"]



&nbsp;   def \_\_init\_\_(self, player1\_name, player2\_name):

&nbsp;       self.player1\_name = player1\_name

&nbsp;       self.player2\_name = player2\_name

&nbsp;       self.player1\_score = 0

&nbsp;       self.player2\_score = 0



&nbsp;   def won\_point(self, player\_name):

&nbsp;       if player\_name == self.player1\_name:

&nbsp;           self.player1\_score += 1

&nbsp;       elif player\_name == self.player2\_name:

&nbsp;           self.player2\_score += 1

&nbsp;       else:

&nbsp;           raise ValueError("Unknown player name")



&nbsp;   def get\_score(self):

&nbsp;       if self.player1\_score == self.player2\_score:

&nbsp;           return self.\_score\_tied()

&nbsp;       if self.player1\_score >= 4 or self.player2\_score >= 4:

&nbsp;           return self.\_score\_end\_game()

&nbsp;       return self.\_score\_normal()



&nbsp;   def \_score\_tied(self):

&nbsp;       if self.player1\_score < 3:

&nbsp;           return f"{self.SCORE\_NAMES\[self.player1\_score]}-All"

&nbsp;       return "Deuce"



&nbsp;   def \_score\_end\_game(self):

&nbsp;       diff = self.player1\_score - self.player2\_score

&nbsp;       if diff == 1:

&nbsp;           return f"Advantage {self.player1\_name}"

&nbsp;       if diff == -1:

&nbsp;           return f"Advantage {self.player2\_name}"

&nbsp;       if diff >= 2:

&nbsp;           return f"Win for {self.player1\_name}"

&nbsp;       return f"Win for {self.player2\_name}"



&nbsp;   def \_score\_normal(self):

&nbsp;       return f"{self.SCORE\_NAMES\[self.player1\_score]}-{self.SCORE\_NAMES\[self.player2\_score]}"





