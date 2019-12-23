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

    def choices(self):
        hand = ''
        if self.cards is None:
            return hand
        else:
            i = 0
            for card in self.cards:
                hand = hand + "[" + str(i) + "] " + str(card) + ", "
                i = i + 1
            hand = hand + '[' + str(i) + '] No Card'
            return(hand)

    def insert_sorted_order(self, new_card, lo, hi):
        mid= floor(lo + (hi-lo)/2)
        if lo > hi:
            # Base case
            self.cards[lo:lo] = [new_card]
        else:
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
        Adds cards to hand in sorted order. Does not sort suits
        Since we know how many cards are in a deck, a better way of keeping
        track of this information would be a dictionary
        '''
        for new_card in new_cards:
            self.insert_sorted_order(new_card, 0, len(self.cards)-1)

    def remove_card(self, index):
        return self.cards.pop(index)


    # def play_cards(self):
    #     I want to play specific cards
    #
    # def sort(self):


class Pile:
    def __init__(self):
        self.cards = []
        self.curr_turn_cards = []
        self.round_value = 0

    def add_cards(self, cards):
        self.cards.append(cards)
        self.curr_turn_cards = cards

    def pick_up(self):
        pile = self.cards
        self.cards = None
        return(pile)

    def change_round(self, val):
        self.round_value = val


    def check_call(self):
        for card in self.curr_turn_cards:
            print(card)
            print("Card Value = " + str(card[0].value) + "  Round Value =" + str(self.round_value) + "\n")
            if card[0].value != self.round_value+1:
                return False
        return True

        # print the cards the player just played and 'Let's see their cards'

        # for loop to go through every card in the curr_turn_cards and see if they match the round value

        # print 'They were lying!' or 'Nice try!'
        # return true if telling truth, return false if lying

        '''
        If we keep track of the round value, then we just need to see if each
        card in the cards played on that turn match the value. We dont need to
        keep track of the call
        '''



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

def player_choose_round_value(limited_value_names, num_sets):
    '''
    Limited value names is the options of card values that the player can play
    given the number of sets in play.
    Num_sets is the number of sets that the player chose to play with in this
    game
    '''
    options = ''
    i = 0
    for name in limited_value_names:
        options = options + "[" + str(i) + "] " + name + ", "
        i = i + 1
    options = options[:-2]
    print('What card value do you want to say these cards were?')
    choice = None

    while choice not in range(0, i):
       try:
          choice = int(input(options + '\n'))
       except ValueError:
          pass

    return HIGHEST_VALUE - num_sets + choice


def player_choose_cards(hand):
    ''''
    This user interaction is really janky, but lemme just get something done

    If user doesnt give any cards this should be considered a pass
    '''
    cards = []
    choice = None
    i = 0
    num_cards_set = len(POSSIBLE_SUITS)
    while i < num_cards_set and len(hand) != 0:
        # ask for card to play
        print(hand.choices())
        choice = ''
        while choice not in range(0, len(hand)+1):
            try:
                choice = int(input('Card? \n'))
            except ValueError:
                pass
        if choice == len(hand):
            i = num_cards_set
            break
            # cards = cards.append([hand.remove_card(choice)])
        cards.append([hand.remove_card(choice)])
        i = i + 1
    return cards

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

def say_call(num_cards, round_value):
    if num_cards == 0:
        print('Pass!')
    else:
        switch = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four'
        }
        call = switch.get(num_cards) + ' ' + POSSIBLE_VALUES_NAMES[round_value] + 's'
        if num_cards == 1:
            call = call[:-1]
        print(call + '!')

def play_bluff_against_comp():
    print('Welcome to bluff!')
    # initiliaze each player
    player_hand = Hand()
    computer_hand = Hand()
    player_list = [player_hand, computer_hand]
    # initiliaze the amount of sets of cards in the game and playable values
    num_sets = player_choose_num_sets()
    limited_value_names = POSSIBLE_VALUES_NAMES[HIGHEST_VALUE - num_sets:
                                                HIGHEST_VALUE]
    short_deck = create_short_deck( num_sets )
    short_deck.shuffle()
    deal_hands(player_list, short_deck)
    pile = Pile()

    turn_cards = player_choose_cards(player_hand)
    pile.change_round(player_choose_round_value(limited_value_names, num_sets))
    say_call(len(turn_cards), pile.round_value)
    # What if You passed! Shouldnt be adding a pass to the pile
    pile.add_cards(turn_cards)
    print(pile.check_call())
    # while in_round:
        # player starts. keep track of who should start.
        # player chooses cards (starter should have to play at least one card)
        # player chooses round value
        # cards are printed to "console"
        # other players can call bluff. [I need to think about this!]
        # could have a players turn function, which takes in a player as a call
        # player 'starter' value could be a boolean variable of the class, and choose card could take it as a function call
        # then we could iterate through a player list
        # if passes equals num_players then start new round
        # instead of having adding player class, i could add these things to hand








    '''
    Brainstorming all the times a round starts and the value needs to be declared

    If all players pass in a row then the last person to play a card starts new round

    If a player correctly guesses a bluff then the guesser starts new round

    If a player incorrectly guesses a bluff then the last player who played a card starts round

    If a new game is started then the first person has to declare the card.


    From this I learned that in more than two players I will need to keep track
    of the last person to play a card. As well as whose turn it is. I could have
    a pass_counter as well, and after someone passes then we check to see if the
    pass_counter == num_players and if it does then the last person who played a
    card starts the round.

    I could have a game class? that keeps track of the information above. And
    then I could have the option of starting a new game.
    That sounds cool. Idk if i need that though

    Todo:
    -

    '''
play_bluff_against_comp()




'''
Below is code used for bug testing
'''

def check_add():
    deck = Deck()
    deck.shuffle()
    hand = Hand()
    i=0
    num_cards=len(deck)
    while i < num_cards:
        new_card = deck.pick_card()
        hand.add_cards([new_card])
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
