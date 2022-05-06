'''Blackjack with a fresh deck on each deal. '''
import random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES =  chr(9824)
CLUBS =  chr(9827)

suits = (HEARTS, DIAMONDS, SPADES, CLUBS)
faces = ('Ace', 'Jack', 'Queen', 'King')

def prepare_deck():
    new_deck = [[i, j] for i in suits for j in range(2, 10)] + [[i, j] for i in suits for j in faces]
    random.shuffle(new_deck)
    return new_deck

def deal(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    print(player_hand)

def play_round():
    deck = prepare_deck()
    deal(deck)

play_round()