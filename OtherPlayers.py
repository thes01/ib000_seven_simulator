from Player import Player
from Helpers import *
 
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
        return False

class SensiblePlayer(Player):
    """
        - 
    """
    def __init__(self, name: str):
        super().__init__(name)

        self.VALUABLE_STARTING_MIN_REPEATABILITY = 2
        self.VALUABLE_RESPONDING_MIN_REPEATABILITY = 2
        self.MIN_STACK_VALUE_TO_REPEAT = 1
        self.STOP_REPEATING_WHEN_WINNING = True

    def startingStrategy(self, card: int):
        if card == 0:
            return 0

        _repeatability = self.cardRepeatingAbility(card)

        if isValuableCard(card) and _repeatability < self.VALUABLE_STARTING_MIN_REPEATABILITY:
            return 0
        
        return _repeatability

    def respondingStrategy(self, card: int, stack):
        if isValuableCard(stack[0]):
            if self.cardRepeatingAbility(stack[0]) >= self.VALUABLE_RESPONDING_MIN_REPEATABILITY:
                if card == stack[0]:
                    return 3
                if card == 0:
                    return 2
                if isValuableCard(card):
                    return 0
                else:
                    return 1
            else:
                # doesn't have enough good cards
                if card == stack[0]:
                    return 2
                if card == 0:
                    return 1
                if isValuableCard(card):
                    return 0
                return 3
        else:
            # the starting card is not valuable
            if card == stack[0]:
                return 3
            if card == 0:
                return 1
            if isValuableCard(card):
                return 0
            else:
                return 2

    def repeatingStrategy(self, card: int, stack):
        if card == stack[0]:
            return 2
        if card == 0:
            return 1
        return -1

    def stopRepeatingCondition(self, stack: list, is_winning: bool):
        """ if this function returns true, then repeating doesn't proceed and directly returns None"""
        if is_winning and self.STOP_REPEATING_WHEN_WINNING:
            return True

        _stack_value = assessCards(stack)
        if _stack_value < self.MIN_STACK_VALUE_TO_REPEAT:
            return True
        
        return False
