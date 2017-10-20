from random import randint
from Helpers import *
from NotifyModule import NotifyModule
 
class Player(NotifyModule):
    def __init__(self, name: str): 
        self.deck = []
        self.hand_cards = []
        self.archive_cards = []
        self.name = name
        self.score = 0

    # return how many cards should be taken, min: 0, max: 4
    @property
    def cards_to_take(self):
        return 4 - len(self.hand_cards)

    def endOfGame(self): 
        self.archive_cards = []
        self.score = 0
    
    def takeCardsFromDeck(self, n: int):
        if (len(self.deck) < n):
            raise IndexError("There is not enough cards in the deck")

        for i in range(n):
            self.hand_cards.append(self.deck.pop())

    def takeToFull(self, first: bool):
        # if this players draws as first then the required count of cards in deck is double (because the second one needs them as well)
        required_deck_length = self.cards_to_take * 2 if first else self.cards_to_take

        if len(self.deck) >= required_deck_length:
            self.takeCardsFromDeck(self.cards_to_take)
        else:
            if first:
                self.takeCardsFromDeck(len(self.deck) // 2) # if players draws first, then the deck length is always even
            else:
                self.takeCardsFromDeck(len(self.deck))

    def collectFromStack(self, stack: list):
        self.score += assessCards(stack)
        # put the cards from current stack to archive
        self.archive_cards.extend(stack)
        stack = []

    def cardRepeatingAbility(self, card: int):
        _count = 0
        for _card in self.hand_cards:
            if _card == 0 or _card == card: 
                _count += 1

        return _count

    def takeBestCard(self, cards:list, mapping_function, **mapping_functions_kwargs):
        # let's assess each card (its attractiveness) and store the key/value in order to get the highest possible
        best_val = -1
        best_index = -1

        self.notify("{}'s cards:".format(self.name),2)

        for i in range(len(cards)):
            result = mapping_function(cards[i], **mapping_functions_kwargs)
            self.notify("score({})={}".format(translateCodeToCard(cards[i]), result), 2)
            if (result > best_val):
                best_val = result
                best_index = i

        if (best_val == -1):
            return None

        best_card = cards[best_index]
        del cards[best_index]
        return best_card

    def playCardStarting(self):
        return self.takeBestCard(self.hand_cards, self.startingStrategy)

    def playCardResponding(self, stack: list):
        return self.takeBestCard(self.hand_cards, self.respondingStrategy, stack=stack)

    def playCardRepeating(self, stack: list, is_winning: bool):
        if (len(self.hand_cards) == 0 or self.stopRepeatingCondition(stack, is_winning)):
            return None

        return self.takeBestCard(self.hand_cards, self.repeatingStrategy, stack=stack)

    # these methods are going to be overridden by child classes

    def startingStrategy(self, card: int):
        return 0

    def respondingStrategy(self, card: int, stack):
        return 0

    def repeatingStrategy(self, card: int, stack):
        if (card == stack[0]):
            return 1
        else: return -1

    def stopRepeatingCondition(self, stack: list, is_winning: bool):
        return False