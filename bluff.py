import itertools
import random
from math import floor

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

    def insert_sorted_order(self, new_card, lo, hi):
        mid= floor(lo + (hi-lo)/2)
        print("lo = " + str(lo) + "   Mid = " + str(mid) + "  hi = " + str(hi))
        if lo > hi:
            # Base case
            self.cards[lo:lo] = [new_card]
        else:
            print("Mid value = " + str(self.cards[mid].value) + "   new card = " + str(new_card.value))

            if self.cards[mid].value == new_card.value:
                # if the value is the same as the midpoint, put card there
                self.cards[mid:mid] = [new_card]
            elif self.cards[mid].value > new_card.value:
                # card value is to the left of mid
                self.insert_sorted_order(new_card, lo, mid-1)
            else:
                # card value is to the right of mid
                self.insert_sorted_order(new_card, mid+1, hi)

    def add_cards(self, new_cards):
        '''
        I want this to add the card in a sorted order. At first I dont care
        about suit. Lets use something like binary search.
        '''
        for new_card in new_cards:
            self.insert_sorted_order(new_card, 0, len(self.cards)-1)

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
    the same value.3
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

def deal_hands( player_list, deck ):
    '''
    Right now I treat hands as players. Later I think I will create a player
    class so that I can hold onto other information. Maybe I wont need it?
    '''
    num_players = len(player_list)
    num_cards = len(deck)
    while (num_cards >= num_players):
        i = 0
        while i < num_players:
            player_list[i].add_cards([deck.pick_card()])
            i = i + 1
            num_cards = num_cards - 1
    print(str(num_cards) + " cards were not dealt.")


def play_bluff_against_comp():
    print('Welcome to bluff!')
    short_deck = create_short_deck( player_choose_num_sets() )
    short_deck.shuffle()
    player_hand = Hand()
    print(player_hand)
    computer_hand = Hand()
    deal_hands([player_hand, computer_hand], short_deck)
    print(player_hand)
    print(computer_hand)


play_bluff_against_comp()
def check_add():
    deck = Deck()
    deck.shuffle()
    hand = Hand()
    i=0
    num_cards=len(deck)
    while i < num_cards:
        new_card = deck.pick_card()
        hand.add_cards([new_card])
        print("i = " + str(i) + "   card = " + str(new_card) + "    hand = " + str(hand))
        i = i + 1
        player_choose_num_sets()

# check_add()
# hand.add_cards([deck.pick_card()])
# print(hand)


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
#     hand1.add_cards([deck.pick_card()])
#     hand2.add_cards([deck.pick_card()])
#     hand3.add_cards([deck.pick_card()])
#     hand4.add_cards([deck.pick_card()])
#     i = i + 1
#
# print(hand4)
