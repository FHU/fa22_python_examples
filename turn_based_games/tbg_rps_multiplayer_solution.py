from turn_based_game import Player, TurnBasedGame
from getpass import getpass

class RpsPlayer(Player):
    def __init__(self, number):
        Player.__init__(self, number)
        self.throw = '' # The player's choice for R/P/S

    def throw_rps(self):
        self.throw = ''
        while self.throw not in 'RPS' or self.throw == '':
            self.throw = getpass(f"What is {self.name}'s throw (R/P/S)? ").upper()

    def __lt__(self, other):
        '''compare either a string or another RpsPlayer'''
        if isinstance(other, RpsPlayer):
            other_throw = other.throw
        else:
            other_throw = other

        if (
            self.throw == "R"
            and other_throw == "P"
            or self.throw == "S"
            and other_throw == "R"
            or self.throw == "P"
            and other_throw == "S"
        ):
            return True
        else:
            return False

    def __gt__(self, other):
        '''compare either a string or another RpsPlayer'''
        if isinstance(other, RpsPlayer):
            other_throw = other.throw
        else:
            other_throw = other

        if (
            self.throw == "P"
            and other_throw == "R"
            or self.throw == "R"
            and other_throw == "S"
            or self.throw == "S"
            and other_throw == "P"
        ):
            return True
        else:
            return False

    def __eq__(self, other):
        '''compare either a string or another RpsPlayer'''
        if isinstance(other, RpsPlayer):
            other_throw = other.throw
        else:
            other_throw = other

        if self.throw == other_throw:
            return True
        else:
            return False

    
class RpsGame(TurnBasedGame):
    player_class = RpsPlayer

    def __init__(self, players: list = None):
        super().__init__(players)
        self.players_out_of_round = []

    def all_throws(self):
        '''return a list of all the throws for this round'''
        return [ player.throw for player in self.players ]

    def max_throw(self):
        '''Return the character for the max throw or None when there is a tie'''
        throw_counts = { throw: self.all_throws().count(throw) for throw in 'RPS' }
        max_throws = [key for key, count in throw_counts.items() if count == max(throw_counts.values())]
        if len(max_throws) == 1:
            return max_throws[0]
        else:
            return None

    def play_round(self):
        for player in self.players:
            player.throw_rps()

        # if only two of the three options are chosen in the group
        # or there are only two players left, remove the loosers
        if len(set(self.all_throws())) == 2 or len(self.players) == 2:
            for player in self.players:
                if player < max(self.players):
                    self.players.remove(player)
                    self.players_out_of_round.append(player)

        # When there is a majority winner, all the losers are out
        if winning_throw := self.max_throw():
            for player in self.players:
                if player < winning_throw:
                    self.players.remove(player)
                    self.players_out_of_round.append(player)

        # select the winner
        if len(self.players) == 1:
            self.winner = self.players[0]


    def start(self):
        super().start()
        self.players += self.players_out_of_round
        self.players_out_of_round = []


if __name__ == "__main__":
    game = RpsGame()
    game.run()