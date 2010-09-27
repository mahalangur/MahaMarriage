# Modified a Random Code off the internet for Marriage!
# OldMaven
# Sept 26, 2010

import random

def new_deck():
    """
    create a deck of cards
    suit: club=C, diamond=D, heart=H spade=S
    rank: ace=A, 10=T, jack=J, queen=Q, king=K, numbers=2..9
    ace of spade would be AS, 8 of heart would be 8H and so on
    return a list of a full deck of cards
    """
    rs = [rank + suit for rank in "A23456789TJQK" for suit in "CDHS"]
    return rs * 3

def draw_cards(n, cards_list):
    """
    randomly draw n cards from the deck (cards_list)
    remove those cards from the deck
    since object cards_list is by reference, it will change too
    return a list of n cards
    """
    random.shuffle(cards_list)
    return [cards_list.pop() for k in range(n)]

# new deck
cards_list = new_deck()
hand = [0,0,0,0,0,0] # Six Players Max

print("3 Decks for Marriage = %s cards" % cards_list)
print("Total Cards = %s cards" % len(cards_list))  # test
# draw n cards per hand
n = 21
# draw the hands
num_of_players = input("How many players do we have? ")
for i in range(0, num_of_players):
    hand[i] = draw_cards(n, cards_list)


print('-'*80)
for j in range(0, num_of_players):
    print("hand[" + str(j) + "] = %s" % hand[j])
print('-'*80)

print("Remaining Cards = %s cards" % cards_list)
print("Remaining Cards = %s cards" % len(cards_list))  # test

