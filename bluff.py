import itertools
import random

"""
@author Julian DeGroot-Lutzner
@date Fall 2019

"""
POSSIBLE_SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
HIGHEST_VALUE = 13
POSSIBLE_VALUES = range(1, HIGHEST_VALUE+1)
POSSIBLE_VALUES_NAMES = ['Ace','Two','Three','Four','Five','Six',
        'Seven','Eight','Nine','Ten','Jack','Queen','King']
NUM_CARDS = HIGHEST_VALUE * len(POSSIBLE_SUITS)


class Card:
    """
    Class to contain the contents of a card.
    Value - the
    """
    def __init__(self, value, suit):

        self.suit = suit
        self.value = value

    def __str__(self):
        return (POSSIBLE_VALUES_NAMES[self.value-1] + ' of ' + self.suit)

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in POSSIBLE_VALUES for suit in POSSIBLE_SUITS]

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def pick_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise IndexError('Trying to deal from an empty deck.')
            # Is this the right way to check for error?


class Hand:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        hand = ''
        if self.cards is None:
            return hand
        else:
            for card in self.cards:
                hand = hand + str(card) + ", "
            hand = hand[:-2]
            return(hand)

    def add_cards(self, cards):
        self.cards.append(cards)

    def remove_cards(self, cards):
        print('not yet')


    # def play_cards(self):
    #     I want to play specific cards
    #
    # def sort(self):


class Pile:
    def __init__(self):
        self.cards = []
        self.curr_turn_cards = []
        self.curr_turn_call = []

    def add_cards(self, cards, call):
        self.card = self.card.append(cards)
        self.curr_turn_call = call
        self.curr_turn_cards = cards

    def pick_up(self):
        pile = self.cards
        self.cards = None
        return(pile)


    # def check_call(self):
        # return true if telling truth, return false if lying



    # def call_bluff(self):
    #
    #     else return

    # def show_call(self, )

class Player:
    def __init__(self, name):
        self.hand = Hand()
        self.name = name

    def print_hand(self):
        print(self.hand)

    def print_name(self):
        print(self.name)






def create_short_deck(num_sets):
    '''
    Takes the number of sets the user wants. A set is four cards from
    the same value.
    num_sets must be in between 1 and 13 inclusive
    '''
    if num_sets > HIGHEST_VALUE or num_sets < 0:
        raise ValueError("Not enough cards available in deck.")
    short_deck = Deck()
    top_cards = []
    size = num_sets * len(POSSIBLE_SUITS)
    while size > 0:
        top_cards.append(short_deck.pick_card())
        size = size - 1
    short_deck.cards = top_cards
    return short_deck


def player_choose_num_sets():
    choice = None
    while choice not in range(1, HIGHEST_VALUE+1):
       try:
          choice = int(input('Number of sets? \n'))
       except ValueError:
          pass
    return choice

def deal_hands():
    print('n')

def play_bluff():
    print('Welcome to bluff!')
    deck = Deck()
    short_deck = create_short_deck( player_choose_num_sets() )
    short_deck.shuffle()

    player_hand = Hand()
    computer_hand = Hand()


play_bluff()
#
# choice = None
# while choice not in [1, 2, 3]:
#    try:
#       choice = int(input('1, 2 or 3? '))
#    except ValueError:
#       pass

# while len(short_deck) > 0:
#     print(short_deck.pick_card())

# hand1.add

#
# num_players = 4
# hand1 = Hand()
# hand2 = Hand()
# hand3 = Hand()
# hand4 = Hand()
# deck = Deck()
# deck.shuffle()
#
# i=0
# while i < NUM_CARDS/num_players:
#     # for player in Players list
#     hand1.add_cards(deck.pick_card())
#     hand2.add_cards(deck.pick_card())
#     hand3.add_cards(deck.pick_card())
#     hand4.add_cards(deck.pick_card())
#     i = i + 1
#
# print(hand4)
