'''An extension of a turn based game, the face card game uses a deck of cards
By convention, the end of a list of cards is considered the top of the pile
'''

from turn_based_game import Player, TurnBasedGame
import random


class Card:
    value_lookup = {14:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K'}

    def __init__(self, suit: str, value: int):
        self.value = value
        self.suit = suit # H heart, D diamond, S spade, C club

    def get_color(self):
        if self.suit in 'HD':
            return 'red'
        else:
            return 'balck'

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False


    def __str__(self):
        return f"{self.suit}{self.value_lookup[self.value]}"

    
class CardDeck:
    card_type = Card
    def __init__(self):
        self.cards = []
        self.discard_pile = []
        for suit in 'HDSC':
            for value in self.card_type.value_lookup:
                self.cards.append(Card(suit, value))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            self.shuffle_in_discard()
        return self.cards.pop()

    def discard(self, card: Card):
        self.discard_pile.append(card)

    def shuffle_in_discard(self):
        random.shuffle(self.discard_pile)
        self.cards = self.discard_pile + self.cards
        self.discard_pile = []


class CardPlayer(Player):
    deck = CardDeck()
    def __init__(self, player_num):
        super().__init__(player_num = player_num)
        self.card_hand = []
        self.card_in_play = None

    def reset(self):
        self.card_hand = []
        self.card_in_play = None
        return super().reset()

    def draw_card(self):
        self.card_hand.append(self.deck.draw_card())

    def take_turn(self):
        '''override for your game rules'''

    def select_card(self):
        card = None
        while not card:
            for index, card in enumerate(self.card_hand):
                print(f"{index}: {card}")
            selection = int(input("Which card do you choose? "))
            if selection in range(0,len(self.card_hand)):
                self.card_in_play = self.card_hand.pop(selection)

    def add_cards_to_hand(self, cards: list):
        self.card_hand = cards + self.card_hand

    def play_top_card(self):
        self.card_in_play = self.card_hand.pop()

    def get_top_card(self):
        return self.card_hand.pop()

    def get_random_card(self):
        return self.card_hand.pop(random.randint(0,len(self.card_hand) - 1))


class CardGame(TurnBasedGame):
    player_class = CardPlayer
    deck = player_class.deck

    def play_round(self):
        for player in self.players:
            player.take_turn()

    def deal(self, card_count=7):
        for _ in range(card_count):
            for player in self.players:
                player.draw_card()
    
    def deal_deck(self):
        '''Deal all the cards in the deck'''
        for num in range(len(self.deck.cards)):
            self.players[num % len(self.players)].draw_card()


if __name__ == "__main__":
    game = CardGame()
    game.run()