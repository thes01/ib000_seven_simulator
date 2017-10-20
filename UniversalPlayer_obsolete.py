from Player import Player
from Helpers import *

class UniversalPlayer(Player):

    def __init__(self, name: str, deck: list):
        super().__init__(name, deck)

        self.__starting_strategy = super().startingStrategy
        self.__responding_strategy = super().respondingStrategy
        self.__repeating_strategy = super().repeatingStrategy
        self.__stop_repeating_condition = super().stopRepeatingCondition

    def setStrategies(self, starting_strategy = None, responding_strategy = None, repeating_strategy = None, stop_repeating_condition = None):
        if starting_strategy != None:
            self.__starting_strategy = starting_strategy
        if responding_strategy != None:
            self.__responding_strategy = responding_strategy
        if repeating_strategy != None:
            self.__repeating_strategy = repeating_strategy
        if stop_repeating_condition != None:
            self.__stop_repeating_condition = stop_repeating_condition

    ### class methods that return current strategies

    def startingStrategy(self, card: int):
        return self.__starting_strategy(card)

    def respondingStrategy(self, card: int, stack):
        return self.__responding_strategy(card, stack=stack)

    def repeatingStrategy(self, card: int, stack):
        return self.__repeating_strategy(card, stack=stack)

    def stopRepeatingCondition(self, stack: list, is_winning: bool):
        return self.__stop_repeating_condition(stack, is_winning)

    def strategy_composite(self, strategies: set):
        def call_func(card: int, **kwargs):
            _total_score = 0

            for strategy in strategies:
                if not callable(strategy):
                    raise TypeError("Strategy must be a callable function")
                _total_score += strategy(card, **kwargs)

            return _total_score

        return call_func

    # strategy 'extensions'

    def preferNonpointers(self, card:int):
        if not isValuableCard(card):
            return 1
        return 0

    def preferPointers(self, card:int):
        if isValuableCard(card):
            return 1
        return 0

    ### starting strategies

    def strategy_starting_1(self, card: int):
        """ 'nonpointer' > 'pointer' > seven """ 
        if card == 0:
            return 0
        if isValuableCard(card):
            return 1
        return 2

    def strategy_starting_2(self, card: int):
        if card == 0:
            return 0

        return self.cardRepeatingAbility(card)

    def strategy_starting_sensible(self, card: int):
        if card == 0:
            return 0

        _repeatability = self.cardRepeatingAbility(card)

        if isValuableCard(card) and _repeatability < 2:
            return 0

        return _repeatability

    ### responding strategies

    def strategy_responding_1(self, card: int, stack):
        """ matching card > 'nonpointer' > 'seven' > 'pointer'"""
        if card == stack[0]:
            return 3
        if card == 0:
            return 1
        if isValuableCard(card):
            return 0
        return 2

    def strategy_responding_only_pointers(self, card: int, stack):
        raise NotImplementedError()

    def strategy_responding_sensible(self, card: int, stack):
        if isValuableCard(stack[0]):
            if self.cardRepeatingAbility(stack[0]) > 1:
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
                if isValuableCard(card) or card == 0:
                    return 0
                return 1
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

    ### repeating strategies

    def strategy_repeating_1(self, card: int, stack):
        """ prefers original cards rather than sevens """
        if card == stack[0]:
            return 2
        if card == 0:
            return 1
        return -1

    def strategy_repeating_3(self, card: int, stack):
        raise NotImplementedError()

    ### stop repeating conditions
    
    def condition_stop_repeating_1(self, stack: list, is_winning: bool):
        """ stops if winning"""
        return is_winning

    def condition_stop_repeating_3(self, stack: list, is_winning: bool):
        _stack_value = assessCards(stack)

        return is_winning or _stack_value == 0