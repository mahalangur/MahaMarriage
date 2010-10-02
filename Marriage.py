# Implementation of Marriage card game in Python
# Originally by Oldmaven

from sys import exit
from random import shuffle

class Marriage:

	def __init__(self, num_of_players):
		self.num_of_players = num_of_players
		self.hand = [0,0,0,0,0,0] # Six Players Max
		rs = [suit + rank for suit in "CDHS" for rank in "A23456789TJQK"]
		self.cards_list = rs * 3

	def print_deck(self):
		print "Deck: %s" % self.cards_list
		print "Total Cards = %s cards" % len(self.cards_list)

	def print_hands(self):
		print '-' * 80
		for j in range(0, self.num_of_players):
			print "hand[" + str(j) + "] = %s" % self.hand[j]
		print '-' * 80

	def draw_cards(self):
		"""
		randomly draw n cards from the deck (cards_list)
		remove those cards from the deck
		since object cards_list is by reference, it will change too
		return a list of n cards
		"""
		n = 21 
		shuffle(self.cards_list)
		return [self.cards_list.pop() for k in range(n)]

	def draw_hands(self):
		for i in range(0, self.num_of_players):
			self.hand[i] = self.draw_cards()

	def sort_hands(self):
		for j in range(0, self.num_of_players):
			self.hand[j] = sorted(self.hand[j])

def main():
	# display error and exit game if invalid number of players
	num_of_players = input("How many players do we have? (1-6) ")
	if not ( num_of_players > 0 and num_of_players < 7):
		print "Number of players must be 1-6!"
		exit()

	# Create instance of Marriage class
	marriage = Marriage(num_of_players)

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
