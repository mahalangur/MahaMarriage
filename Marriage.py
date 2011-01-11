# Implementation of Marriage card game in Python
# Originally by Oldmaven

from sys import exit
from random import shuffle

#let them be global vars
cards_to_deal = 21
max_players  = 6
number_of_decks = 3

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
    return '\t'.join(res)
    
  def pop_card(self):
    return self.cards.pop()
    
  def add_card(self, card):
    self.cards.append(card)
    
  def shuffle(self): 
    shuffle(self.cards)


class Hand(Deck):

  def __init__(self): 
    self.cards = []

  def as_dict(self):
   dict = {}
   for card in self.cards:
     if (card.suit,card.rank) in dict:
       dict[(card.suit, card.rank)] += 1
     else:
       dict[(card.suit, card.rank)] = 1
   return dict

  def is_tanela(self,lst):
    """lst is a list of cards"""
    return len(lst)==3 and all(l == lst[0] for l in lst[1:])

  def is_puresequence(self,lst):
    """lst is a list of cards"""
    
  def detecttanela(self):
    dict = self.as_dict()
    return [Card(key[0],key[1]) for key in dict if  dict[key] == 3]
        
  def detectpuresequence(self):
    dict = self.as_dict()
    ret = []
    for n in range(4): # should be safe since suits never increase
      lst = [k[1] for k in dict if k[0] ==n].sort() # returns a row of unique rank of the same suit
      ret.append([Card(n,r) for r in self.showruns(lst)])
    return ret
  
  def detectcombos():
    """returns a list of combo objs"""


#utility fns maybe refactor later?
  def showruns(self, lst, n):
    """
      shows a list of at least n consecutive numbers in any array
      self.showruns([1,2,3,5,6,7,8,9,11],3) => [[1,2,3],[5,6,7,8,9]]

      not efficient but works
    """
    ret = []
    help = self.showarrayrun_helper([],lst,n) 
    while True:
      if help[0]:
        ret.append(help[0])
      if not help[1]:
        break
      else:
        help = self.showarrayrun_helper([],help[1],n)
    return ret

  def showruns_helper(self, acc, lst, len):
    if lst and (not acc or (acc[-1]+1 == lst[0])):
        return self.showarrayrun_helper(acc+lst[0:1], lst[1:], len - 1)
    else:
        return ([],lst) if len > 0 else (acc,lst)

class Marriage:
	def __init__(self, num_of_players):
		self.num_of_players = num_of_players
		self.deck = Deck(number_of_decks)
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

#for testing purposes...
m = Marriage(4)
m.draw_hands()
m.sort_hands()
h = m.hands[0]



if __name__ == '__main__':
	main()
