# Make a RPS game that one player plays against the computer
import random

random.choice("RPS")

class RockPaperScissors():
    def __init__(self):
        self.winner = ''

    def play(self):
        print("Lets play Rock Paper Scissors!!")
        while not self.winner:
            selection = input("What would you like to throw (R/P/S)? ").upper()
            comp_sel = random.choice("RPS")
            if selection in "RPS":
                if selection == comp_sel:
                    print(f"You both threw {selection}")
                elif selection == "R" and comp_sel == "P" or selection == "S" and comp_sel == "R" or selection == "P" and comp_sel == "S":
                    self.winner = 'computer'
                else:
                    self.winner = 'player'
                print(f"You threw {selection} and the computer threw {comp_sel}")
                self._announce_winner()
            else:
                print("That is not an option :(")


    def _announce_winner(self):
        print(f"The winner is {self.winner}")


if __name__ == "__main__":
    rps = RockPaperScissors()
    rps.play()