# Make a Rock Paper Scissors game with one player playing a computer

import random

class RockPaperScissors():
    def __init__(self):
        self.winner = ''

    def play(self):
        print("Lets play Rock Paper Scissors!")
        while not self.winner:
            selection = input("What would you like to throw (R/P/S)? ").upper()
            if selection in "RPS":
                comp_sel = random.choice("RPS")
                if selection == comp_sel:
                    print(f"You both played {selection}")
                elif selection == 'R' and comp_sel == 'S':
                    print(f"Your Rock beat the computer's Scissors")
                    self.winner = 'player'
                elif selection == 'S' and comp_sel == 'R':
                    print(f"The computer's Rock beat your Scissors")
                    self.winner = 'computer'
                elif selection == 'S' and comp_sel == 'P':
                    print(f"Your Scissors beat the computer's Paper")
                    self.winner = 'player'
                elif selection == 'P' and comp_sel == 'S':
                    print(f"The computer's Scissors beat your Paper")
                    self.winner = 'computer'
                elif selection == 'P' and comp_sel == 'R':
                    print(f"Your Paper beat the computer's Rock")
                    self.winner = 'player'
                elif selection == 'R' and comp_sel == 'P':
                    print(f"The computer's Paper beat your Rock")
                    self.winner = 'computer'
            else:
                print("That is not an option")

    def _announce_winner(self):
        print(f"The winner is {self.winner}")



if __name__ == "__main__":
    rps = RockPaperScissors()
    rps.play()