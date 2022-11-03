import random

class RockPaperScissors():
    def __init__(self):
        self.winner = ''
        self.comp_sel = ''
        self.player_sel = ''

    def play(self):
        print("Lets play Rock Papaer Scissors!!")
        while not self.winner:
            self._player_go()
            self._comp_go()
            self._check_win()
            self._announce_winner()

    def _player_go(self):
        self.player_sel = input('What would you like to throw (R/P/S)? ').upper()

    def _comp_go(self):
        self.comp_sel = random.choice("RPS")

    def _check_win(self):
        if self.comp_sel == "R" and self.player_sel == "S" or self.comp_sel == "S" and self.player_sel == "P" or self.comp_sel == "P" and self.player_sel == "R":
            self.winner = "computer"
        elif self.comp_sel == self.player_sel:
            self.winner = ''
        else:
            self.winner = 'player'

    def _announce_winner(self):
        print(f"Player threw {self.player_sel}!")
        print(f"Computer threw {self.comp_sel}!")
        if self.winner == '':
            print("TIE - try again")
        else:
            print(f"{self.winner} wins!!")


if __name__ == "__main__":
    rps = RockPaperScissors()
    rps.play()