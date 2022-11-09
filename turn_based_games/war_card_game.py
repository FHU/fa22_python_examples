from face_card_game import CardGame
import random
import time

class War(CardGame):
    def __init__(self, players: list = None):
        super().__init__(players)
        self.players_out = []

    def check_finish(self):
        if len(self.players) == 1:
            self.winner = self.players[0]
        return super().check_finish()

    def play_round(self):
        cards_in_play = []
        
        players_in_round = self.players[:]
        cards_to_capture = []

        while len(players_in_round) > 1:
            for player in players_in_round[:]:
                if len(player.card_hand) == 0:
                    players_in_round.remove(player)
                    self.players.remove(player)
                    self.players_out.append(player)
                    print(f"Player removed: {player.name}")
                    time.sleep(1)
            if len(players_in_round) == 1:
                round_winner = players_in_round[0]
                break
            for player in players_in_round:
                player.play_top_card()
                cards_in_play.append(player.card_in_play)

            # Case one max
            if cards_in_play.count(max(cards_in_play)) == 1:
                round_winner = self.players[cards_in_play.index(max(cards_in_play))]
                cards_to_capture += cards_in_play
                break
            # Case at least one tie
            else:
                for player in players_in_round[:]:
                    if player.card_in_play != max(cards_in_play):
                        players_in_round.remove(player)
                    else:
                        # each player gives up 3 cards to the winner
                        extra_card_count = 5 - len(self.players) if len(self.players) < 5 else 1
                        for _ in range(extra_card_count):
                            if len(player.card_hand) > 1:
                                cards_to_capture.append(player.get_top_card())

                cards_to_capture += cards_in_play
                cards_in_play = []
        random.shuffle(cards_to_capture) # Without shuffling, we got into infinite loops occasionally
        round_winner.add_cards_to_hand(cards_to_capture)
        print(f"This battle goes to {round_winner.name}")
        print(f'cards captured: {" ".join([ str(card) for card in cards_to_capture])}')
        time.sleep(.2)

        return super().play_round()

    def start(self):
        super().start()
        self.players += self.players_out
        self.players_out = []
        self.deck.__init__()
        self.deal_deck()

if __name__ == "__main__":
    game = War()
    game.run()