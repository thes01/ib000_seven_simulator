from Player import Player
from Helpers import isValuableCard

class PlayerLevelOne(Player):
    """
        This is the most basic player:
            - starting with a random card
            - when responding, tries to find matching card (not sevens), otherwise plays a random
            - repeating only if loosing
    """

    def respondingStrategy(self, card:int, stack):
        if (card == stack[0]):
            return 1
        return 0

class PlayerLevelTwo(Player):
    """
        A player better than basic:
            - starting priority: 'nonpointer' > 'pointer' > seven
            - responding: matching card > 'nonpointer' > 'seven' > 'pointer' - not aggressive
    """

    def startingStrategy(self, card: int):
        # seven is not good for start, as well as 10 or A, so best are the 'nonpointers'
        if card == 0:
            return 0
        if isValuableCard(card):
            return 1
        return 2

    def respondingStrategy(self, card: int, stack):
        if card == stack[0]:
            return 3
        if card == 0:
            return 1
        if isValuableCard(card):
            return 0
        return 2

    def repeatingStrategy(self, card: int, stack):
        if card == stack[0]:
            return 2
        if card == 0: # seven
            return 1
        return -1

class PlayerLevelThree(Player):
    """
        - starting priority - prefers the most repeatable cards
        - responding - similar
        - repeating if has enough cards even if it is winning
    """
    def startingStrategy(self, card:int):
        if card == 0:
            return 0
        if isValuableCard(card):
            return self.cardRepeatingAbility(card)

        return 2 + self.cardRepeatingAbility(card)

    def respondingStrategy(self, card:int, stack):
        if card == stack[0]:
            return 3
        if card == 0:
            return 1
        if isValuableCard(card):
            return 0
        else: 
            return 2

    def repeatingStrategy(self, card:int, stack):
        if card == stack[0]:
            return 2
        if card == 0: # seven
            return 1
        return -1
    
    def stopRepeatingCondition(self, stack: list, is_winning: bool):
        return len(self.hand_cards) == 0

class PlayerLevelThreeNonAggressive(PlayerLevelThree):
    def stopRepeatingCondition(self, stack: list, is_winning: bool):
        return len(self.hand_cards) == 0 or not isValuableCard(stack[0])