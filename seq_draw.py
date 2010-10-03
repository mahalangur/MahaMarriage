from sys import exit
from random import shuffle

num_of_players = input("How many players do we have? (1-5) ")
if not ( num_of_players > 0 and num_of_players < 6):
	print "Number of players must be 1-5!"
	exit()
rs = [suit + rank for suit in "CDHS" for rank in "A23456789TJQK"]
deck = rs * 3
print "printing deck"
print '='*80
print deck
print '='*80
print "Shuffling Deck"
shuffle(deck)
print deck
print '='*80
print "No. of cards in deck is", len(deck)
print "***Distributing cards***"
print "="*80

for i in range(0,num_of_players):
	exec 'hand%d = []' % i
for j in range(0,21):
		for i in range(0,num_of_players):
			item = deck.pop()
			code = 'hand%d.insert(j, item)' % i
			exec code
	
print "Remaining deck"
print "="*80
print deck
print "No. of cards in deck is",len(deck)
print "="*80

for i in range(0,num_of_players):
	hand_num = 'hand_%d' %i
	code = "print hand_num,'=', sorted(hand%d)" %i
	exec code
