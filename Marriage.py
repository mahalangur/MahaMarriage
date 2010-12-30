# Implementation of Marriage card game in Python
# Originally by Oldmaven

from sys import exit
from random import shuffle

#let them be global vars
cards_to_deal = 21
max_players  = 6

class Player:
  def __init__():
    self.cards = []
  
  def addcard(card):
    self.cards.append(card)
  
  def isRobot():
    False

class Card(object):
  """represents a standard playing card."""
  
  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
    
  def __init__(self, suit=0, rank=2):
    self.suit = suit 
    self.rank = rank
  
  def __str__(self): 
    return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
  def __cmp__(self, other):
    t1 = self.suit, self.rank 
    t2 = other.suit, other.rank 
    return cmp(t1, t2)



class Deck(object):
  def __init__(self, times=1): 
    self.cards = []
    for suit in range(4): 
      for rank in range(1, 14):
        card = Card(suit, rank)
        self.cards.append(card)
    self.cards = self.cards * times
    
        
  def move_cards(self, hand, num): 
    for i in range(num):
      hand.add_card(self.pop_card())
            
  def __str__(self):
    res=[]
    for card in self.cards:
      res.append(str(card))
    return '\n'.join(res)
    
  def pop_card(self):
    return self.cards.pop()
    
  def add_card(self, card):
    self.cards.append(card)
    
  def shuffle(self): 
    shuffle(self.cards)

class Hand(Deck):
  def __init__(self): 
    self.cards = []
  
class Marriage:
	def __init__(self, num_of_players):
		self.num_of_players = num_of_players
		self.deck = Deck(3)
		self.hands = []
		for i in range(num_of_players):
		  self.hands.append(Hand())
		

	def print_deck(self):
		print "Deck: %s" % self.deck
		print "Total Cards = %s cards" % len(self.deck.cards)

	def print_hands(self):
		for ahand in self.hands:
		  print '-' * 80
		  print ahand
		  print '-' * 80

	def draw_hands(self):
		"""
		randomly draw n cards from the deck (cards_list)
		remove those cards from the deck
		since object cards_list is by reference, it will change too
		return a list of n cards
		"""
		self.deck.shuffle()
		for ahand in self.hands:
		  self.deck.move_cards(ahand, cards_to_deal)

	def sort_hands(self):
	  for ahand in self.hands:
	    ahand.cards = sorted(ahand.cards)

def main():
	# display error and exit game if invalid number of players
	num_of_players = input("How many players do we have? (1-6) ")
	if not ( num_of_players > 0 and num_of_players < (max_players +1)):
		print "Number of players must be 1-6!"
		exit()

	# Create instance of Marriage class
	marriage = Marriage(num_of_players)
	
	print "\n"
	print " %s hands created " % len(marriage.hands)

	# print current card deck
	print "\n"
	marriage.print_deck()

	# draw hands
	print "\n"
	print "Drawing hands........."
	marriage.draw_hands()

	# print current card deck after drawing hand
	print "\n"
	marriage.print_deck()
	
	print "\n"
	for ahand in range(len(marriage.hands)):
	  print "hand has %s cards" % len(marriage.hands[ahand].cards)

	# print unsorted hands
	print "\n"
	print "Unsorted hands"
	marriage.print_hands()

	# sort hands
	marriage.sort_hands()

	# print sorted hands
	print "\n"
	print "Sorted hands"
	marriage.print_hands()

if __name__ == '__main__':
	main()
