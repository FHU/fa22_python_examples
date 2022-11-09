from turn_based_game import Player, TurnBasedGame
import random

class RpsPlayer(Player):
    def __init__(self, number):
        Player.__init__(self, number)



class RpsGame(TurnBasedGame):
    player_class = RpsPlayer

    def play_round(self):
        ...
    
    

if __name__ == "__main__":
    game = RpsGame()
    game.run()