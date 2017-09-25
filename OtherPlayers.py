from Player import Player

class BasicPlayer(Player):
    def playCardStarting(self):
        # now play a random card
        return self.hand_cards.pop()

    def playCardResponding(self, stack):
        # same type ? random
        ideal_card = self.tryToPopFromHands(stack[0])

        if ideal_card is None:
            return self.hand_cards.pop()
        else:
            return ideal_card

    def playCardRepeating(self, stack, is_winning):
        if (is_winning or len(self.hand_cards) == 0):
            return None

        return self.tryToPopFromHands(stack[0])

class BasicPlusPlayer(Player):
    def startingCardAttractivity(self, card):
        # seven is not good for start, as well as 10 or A, so best are the 'nonpointers'
        if (card == 0):
            return 0
        if (card == 3 or card == 7):
            return 1
        return 2

    def playCardStarting(self):
        # lets assess each card (its attractivity) and store the key/value in order to get the hightest possible
        best_val = -1
        best_index = -1

        for i in range(len(self.hand_cards)):
            if (self.startingCardAttractivity(self.hand_cards[i]) > best_val):
                best_val = self.startingCardAttractivity(self.hand_cards[i])
                best_index = i

        best_card = self.hand_cards[best_index]
        del self.hand_cards[best_index]

        return best_card

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