from random import randint
from enum import Enum

# This class has all the components necessary to be fully functioning
# but lacks implementation of certain methods. You should go through
# and try to add the proper functionality to the methods that say
# Implement this!
#
# For further practice, you might try adding more functionality, such
# as giving cards an additional attribute isShowing which is a boolean
# determining whether the card is face up or face down. You can then
# implement a feature of the score property of the Hand class which
# can optionally choose to only get the score of face up cards.

class Number(Enum):
    """
    An Enum which lists the numbers a card can have, ranging from
    Ace through King. Each Enum member has two parameters: the name
    of the number (e.g., 'Ace' or 'Three' or 'Queen') and the value
    it holds in Black Jack. Ace is treated as an 11.
    """
    ACE      = ('Ace', 11)
    TWO      = ('Two', 2)
    THREE    = ('Three', 3)
    FOUR     = ('Four', 4)
    FIVE     = ('Five', 5)
    SIX      = ('Six', 6)
    SEVEN    = ('Seven', 7)
    EIGHT    = ('Eight', 8)
    NINE     = ('Nine', 9)
    TEN      = ('Ten', 10)
    JACK     = ('Jack', 10)
    QUEEN    = ('Queen', 10)
    KING     = ('King', 10)

    def __init__(self, numberName, numberValue):
        self.numberName = numberName
        self.numberValue = numberValue

class Suit(Enum):
    SPADES   = 'Spades'
    CLUBS    = 'Clubs'
    DIAMONDS = 'Diamonds'
    HEARTS   = 'Hearts'

class Card(object):

    def __init__(self, number, suit):
        #Implement this!
        self.number = number
        self.suit = suit

    def __str__(self):
        return self.number.numberName + ' of ' + self.suit.value

    @property
    def value(self):
        return self.number.numberValue

    def isAce(self):
        """
        Determines if the current card is an Ace or not. Necessary
        for knowing if the card's value could be different, depending
        on the score of the hand.
        """
        #Implement this!
        if self.number.numberName == 'Ace':
            self.is_Ace = 1
        else:
            self.is_Ace = 0

import itertools as it
class Deck(object):

    def __init__(self):
        self.deck = []
        self.__populateDeck()
        self.__shuffleDeck()

    def __populateDeck(self):
        """
        Adds all 52 cards to the deck.
        """
        #Implement this!
        for cardinfo in it.product(Number, Suit):
            self.deck.append(Card(cardinfo[0],cardinfo[1]))
    
    def __shuffleDeck(self):
        for i in range(len(self.deck)*20):
            pos1 = randint(0,len(self.deck)-1)
            pos2 = randint(0,len(self.deck)-1)
            temp = self.deck[pos1]
            self.deck[pos1] = self.deck[pos2]
            self.deck[pos2] = temp

    def __str__(self):
        if len(self.deck) == 0:
            return 'Deck is empty'
        
        cardStr = ''
        for card in self.deck:
            cardStr += card.__str__() + '\n'
        return cardStr

    def drawCard(self):
        card = self.deck.pop()
        if len(self.deck) == 0:
            self.__populateDeck()
            self.__shuffleDeck()
        return card
    
class Hand(object):

    def __init__(self, deck):
        self.deck = deck
        self.hand = []

    def drawCard(self):
        self.hand.append(self.deck.drawCard())

    def __str__(self):
        if len(self.hand) == 0:
            return 'Hand is empty'
        
        cardStr = ''
        for card in self.hand:
            cardStr += card.__str__() + '\n'
        return cardStr

    def clearHand(self):
        self.hand = []
    
    @property
    def score(self):
        """
        Returns the total score of all the cards in the player's hand.
        Should count Aces as 11 unless the score is over 21 in which case
        only so many Aces should count as 1 as to keep the score under 21.
        Optional implementation is to allow for getting the score of only
        face up cards, presuming cards have an attribute for determining this.
        """
        #Implement this!
        if len(self.hand) == 0:
            print('score is zero')
            return 0
        else:
            score = 0
            for card in self.hand:
                score += card.value
        if score > 21:
            a_num = self.getNumbOfAces()
            if a_num == 0:
                print('Score = '+str(score))
                return score
            else:
                small_aces = 0
                while score > 21 and small_aces<=a_num:
                    score -= 10
                    small_aces += 1
                print('Score = '+str(score))
                return score
        else:
            print('Score = '+str(score))
            return score
    def getNumbOfAces(self):
        """
        Returns the number of Aces in the hand.
        """
        #Implement this!
        acenum = 0
        for card in self.hand:
            card.isAce()
            if card.is_Ace:
                acenum += 1
        return acenum
                
a_deck = Deck()
hand = Hand(a_deck)











