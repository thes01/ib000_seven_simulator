from Helpers import getCardsString
from NotifyModule import NotifyModule

class Match(NotifyModule):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.winning = first
        self.stack = []

    @property
    def looser(self):
        if (self.winning == self.first):
            return self.second

        return self.first

    def evaluateWinning(self):
        firsts_card = self.stack[-2] # a card played by first i.e. second player
        seconds_card = self.stack[-1]

        if (firsts_card == seconds_card or seconds_card == 0):
            # second has won
            self.winning = self.second
        else:
            self.winning = self.first

        self.notify("Player {} is winning after this round".format(self.winning.name))

    def playMatch(self):
        # play the first round
        self.notify("First round of this match!")

        self.stack.append(self.first.playCardStarting())
        self.stack.append(self.second.playCardResponding(self.stack))
        self.notifyCards(self.stack)

        # update winning status
        self.evaluateWinning()

        # now ask if the first player wants a new round
        repeat_card = self.first.playCardRepeating(self.stack, self.winning == self.first)
        self.notify("repeat_card is {}, winning is first? {}".format(repeat_card, self.winning == self.first))

        while repeat_card != None:
            # first player has started a new round
            self.notify("New round of this match!")
            self.stack.append(repeat_card)
            self.stack.append(self.second.playCardResponding(self.stack))
            self.notifyCards(self.stack)

            self.evaluateWinning()

            repeat_card = self.first.playCardRepeating(self.stack, self.winning == self.first)

        # end of match
        # the winning player should collect the cards from stack and add to his 'archive'
        self.notify("End of match..")

        self.winning.collectFromStack(self.stack) # this also empties the stack

        for _player in [self.first, self.second]:
            self.notify("Player {} has {} points".format(_player.name, _player.score)

        return (self.winning, self.looser)