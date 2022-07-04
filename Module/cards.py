# Add imports here
from random import sample

# Open the file cards.py, and write a function that takes as arguments a list of suits and a list of ranks.
# Inside the function create the list of the deck and return a random group of 4 cards.
#
# The output should be in the format of <rank>-<suit>, e.g Jack-Hearts

# Complete the function
def cards_sample(suits, ranks):
    deck=[str(x)+'-'+y for x in ranks for y in suits]
    return sample(deck,4)



suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [i for i in range(1, 11)] + ['Jack', 'Queen', 'King']

print(cards_sample(suits, ranks))
