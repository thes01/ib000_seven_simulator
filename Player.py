from random import randint
from Helpers import assessCards

class Player:
    def __init__(self, name, deck):
        self.deck = deck
        self.my_cards = []
        self.my_archive = []
        self.name = name

    def score(self):
        return assessCards(self.my_archive)

    # return how many cards should be taken, min: 0, max: 4
    def cardsToTake(self):
        return 4 - len(self.my_cards)
    
    # ! not protected if deck is empty
    def takeCardsFromDeck(self, n):
        print("Player {} takes {} cards from the deck({})".format(self.name, n, len(self.deck)))
        for i in range(n):
            self.my_cards.append(self.deck.pop())
        print("There is now {} cards in his hands".format(len(self.my_cards)))

    def takeToFull(self, first):
        # if this players draws as first then the required count of cards in deck is double (because the second one needs them as well)
        required_deck_length = self.cardsToTake() * 2 if first else self.cardsToTake()

        if len(self.deck) >= required_deck_length:
            self.takeCardsFromDeck(self.cardsToTake())
        else:
            if first:
                self.takeCardsFromDeck(len(self.deck) // 2) # if players draws first, then the deck length is always even
            else:
                self.takeCardsFromDeck(len(self.deck))

    def tryToPopFromHands(self, wanted_card): # TODO: allow sevens
        for i in range(len(self.my_cards)):
            if self.my_cards[i] == wanted_card:
                del self.my_cards[i] # delete the wanted card from my_cards and return it
                return wanted_card
            
        # no card of same type found in hands
        return None

    def collectFromStack(self, stack):
        self.my_archive.extend(stack)
        stack = []

    # these three methods are going to be overridden by child objects

    def playCardStarting(self):
        # now play a random card
        return self.my_cards.pop()

    def playCardResponding(self, stack):
        # same type ? random
        ideal_card = self.tryToPopFromHands(stack[0])

        if ideal_card is None:
            return self.my_cards.pop()
        else:
            return ideal_card

    def playCardRepeating(self, stack, is_winning):
        if (is_winning or len(self.my_cards) == 0):
            return None

        return self.tryToPopFromHands(stack[0])