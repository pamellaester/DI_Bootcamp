import random

class Card(object):

    def __init__(self, value, suit):

        self.value = value

        self.suit = suit

SUITS = 'Hearts Diamonds Clubs Spades'.split()

VALUES = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()



class deck():
  
  @staticmethod
  def suflle():
     assert len(deck) == 52
     return random.shuffle(deck)




print(deck)