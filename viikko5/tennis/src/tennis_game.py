class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_names = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score_when_tied(self, score):
        if score < 3:
            return f"{self.score_names[score]}-All"
        return "Deuce"

    def score_when_end_game(self):
        minus_result = self.player1_score - self.player2_score

        if minus_result == 1:
            score = f"Advantage {self.player1_name}"
        elif minus_result == -1:
            score = f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            score = f"Win for {self.player1_name}"
        else:
            score = f"Win for {self.player2_name}"
        return score

    def score_normal(self):
        return f"{self.score_names[self.player1_score]}-{self.score_names[self.player2_score]}"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.score_when_tied(self.player1_score)

        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.score_when_end_game()
        return self.score_normal()
