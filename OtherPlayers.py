from Player import Player

class PlayerLevelOne(Player):
    """
        This is the most basic player:
            - starting with a random card
            - when responding, tries to find matching card (not sevens), otherwise plays a random
            - repeating only if loosing
    """

    def playCardStarting(self):
        # now play a random card
        return self.hand_cards.pop()

    def playCardResponding(self, stack: list):
        # same type ? random
        ideal_card = self.tryToPopFromHands(stack[0])

        if ideal_card is None:
            return self.hand_cards.pop()
        else:
            return ideal_card

    def playCardRepeating(self, stack: list, is_winning: bool):
        if (is_winning or len(self.hand_cards) == 0):
            return None

        return self.tryToPopFromHands(stack[0])

class PlayerLevelTwo(Player):
    """
        A player better than basic:
            - starting priority: 'nonpointer' > 'pointer' > seven
            - responding: matching card > (-||-)
    """

    def startingCardAttractivity(self, card: int):
        # seven is not good for start, as well as 10 or A, so best are the 'nonpointers'
        if (card == 0):
            return 0
        if (card == 3 or card == 7):
            return 1
        return 2

    def getBestCard(self, cards: list, mapping_function):
        # lets assess each card (its attractivity) and store the key/value in order to get the highest possible
        best_val = -1
        best_index = -1

        for i in range(len(cards)):
            if (mapping_function(cards[i])) > best_val):
                best_val = mapping_function(cards[i])
                best_index = i

        best_card = cards[best_index]
        del cards[best_index]

    def playCardStarting(self):
        return self.getBestCard(self.my_cards, self.startingCardAttractivity)

    def playCardResponding(self, stack):
        # same type ? random
        ideal_card = self.tryToPopFromHands(stack[0])

        if ideal_card is None:
            return self.playCardStarting()
        else:
            return ideal_card

    def playCardRepeating(self, stack, is_winning):
        if (is_winning or len(self.hand_cards) == 0):
            return None

        return self.tryToPopFromHands(stack[0])