from turn_based_game import Player, TurnBasedGame
from getpass import getpass


class RpsPlayer(Player):
    def __init__(self, number):
        Player.__init__(self, number)
        self.throw = ""

    def throw_down(self):
        self.throw = ""
        while self.throw not in "RPS" or self.throw == "":
            self.throw = getpass(f"{self.name}'s choice (R/P/S): ").upper()


class RpsGame(TurnBasedGame):
    player_class = RpsPlayer

    def play_round(self):
        for player in self.players:
            player.throw_down()

        if self.players[0].throw == self.players[1].throw:
            print(f"You both threw {self.players[0].throw}")
        elif (
            self.players[0].throw == "R"
            and self.players[1].throw == "P"
            or self.players[0].throw == "S"
            and self.players[1].throw == "R"
            or self.players[0].throw == "P"
            and self.players[1].throw == "S"
        ):
            self.winner = self.players[1]
        else:
            self.winner = self.players[0]


if __name__ == "__main__":
    game = RpsGame(min_players=2, max_payers=2)
    game.run()
