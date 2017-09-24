from random import randint

class Player:
    def __init__(self, name, deck):
        self.deck = deck
        self.my_cards = []
        self.my_archive = []
        self.name = name

    def score(self):
        _score = 0
        # iterate through current archive cards and count 10s and As - each for 1 point
        for card in self.my_archive:
            if card == 3 or card == 7:
                _score += 1
        return _score

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
        # check if all is ok
        if self.cardsToTake() > 0: print("Error: Player {} hasn't enough cards to play".format(self.name))

        for i in range(4):
            if self.my_cards[i] == wanted_card:
                return self.my_cards.pop(i)
            
        # no card of same type found in hands
        return None

    def collectFromStack(self, stack):
        self.my_archive.extend(stack)
        stack = []

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
        if (is_winning or len(self.my_cards) == 0)
            return None

        return self.tryToPopFromHands(stack[0])