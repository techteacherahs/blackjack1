'''Blackjack with a fresh deck on each deal. '''
import random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES =  chr(9824)
CLUBS =  chr(9827)

suits = (HEARTS, DIAMONDS, SPADES, CLUBS)
faces = ('A', 'J', 'Q', 'K')

def prepare_deck():
    new_deck = [[i, j] for i in suits for j in range(2, 11)] + [[i, j] for i in suits for j in faces]
    random.shuffle(new_deck)
    return new_deck

def display(cards):
    card_parts = ['', '', '', '']
    for card in cards:
        card_parts[0] += '----  '
        card_parts[1] += f'|{card[0]} |  '
        if card[1] == 10:
            card_parts[2] += f'|{card[1]}|  '
        else:
            card_parts[2] += f'| {card[1]}|  '
        card_parts[3] += '----  '

    for part in card_parts:
        print(part)

def score_hand(cards):
    score = 0
    aces = 0
    for card in cards:
        if card[1] in ('K', 'Q', 'J'):
            score += 10
        elif card[1] == 'A':
            aces += 1
        else:
            score += card[1]
    for i in range(aces):
        if score + 11 > 21:
            score += 1
        else:
            score += 11
    return score

def play_round():
    deck = prepare_deck()
    #The following two lines were in function 'deal' but may make more sense here
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    display(player_hand)

    #player decides to accept a new card
    while True:
        accept_card = input("Do you want a card? (y/n) ")
        if accept_card == 'n':
            break
        elif accept_card == 'y':
            player_hand.append(deck.pop())
            display(player_hand)
        else:
            print('Please only enter y or n.')
        p_score = score_hand(player_hand)
        if p_score > 21:
            print(f"Player goes bust with {p_score}")
            return 'Player loses'
    p_score = score_hand(player_hand)
    print(f"Player score: {p_score}")

    while True:
        d_score = score_hand(dealer_hand)
        if d_score < 17:
            dealer_hand.append(deck.pop())
        elif d_score > 21:
            print(f"Dealer goes bust with {d_score}")
            display(dealer_hand)
            return 'Dealer loses'
        else:
            break

    display(dealer_hand)
    print(f"Dealer: {d_score}")
    if d_score < p_score:
        return 'Player wins!'
    elif d_score > p_score:
        return 'Dealer wins :('
    else:
        return 'Tie'


while True:
    play = input('Do you wish to play Blackjack? (y/n) ')
    if play == 'y':
        result = play_round()
        print(result)
    else:
        print('Thanks for stopping by.')
        break