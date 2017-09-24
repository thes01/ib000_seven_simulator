from Helpers import printCards

class Match:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.winning = first
        self.stack = []

    def evaluateWinning(self):
        firsts_card = self.stack[-2] # a card played by first i.e. second player
        seconds_card = self.stack[-1]

        if (firsts_card == seconds_card or seconds_card == 0):
            # second has won
            self.winning = self.second
        else:
            self.winning = self.first

        print("Player {} is winning after this round".format(self.winning.name))

    def playMatch(self):
        # play the first round
        print("First round of this match!")
        self.stack.append(self.first.playCardStarting())
        self.stack.append(self.second.playCardResponding(self.stack))
        printCards(self.stack)
        # update winning status
        self.evaluateWinning()

        # now ask if the first player wants a new round
        repeat_card = self.first.playCardRepeating(self.stack, self.winning == self.first)

        while repeat_card is not None:
            # first player has started a new round
            print("New round of this match!")
            self.stack.append(repeat_card)
            self.stack.append(self.second.playCardResponding(self.stack))
            printCards(self.stack)

            self.evaluateWinning()

            repeat_card = self.first.playCardRepeating(self.stack, self.winning == self.first)

        # end of match
        # the winning player should collect the cards from stack and add to his 'archive'
        print("End of match..")

        self.winning.collectFromStack(self.stack) # this also empties the stack

        for _player in [self.first, self.second]:
            print("Player {} has {} points".format(_player.name, _player.score()))