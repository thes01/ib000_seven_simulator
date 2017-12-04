from Helpers import *
from Notifier import Notifier
from Player import Player


class Match():
    def __init__(self, starting_player: Player, responding_player: Player):
        self.starting_player = starting_player
        self.responding_player = responding_player
        self.winning = starting_player
        self.stack = []
        self.notifier = Notifier()

    @property
    def looser(self):
        if (self.winning == self.starting_player):
            return self.responding_player

        return self.starting_player

    def evaluateWinning(self):
        starting_card = self.stack[0]  # a card played by starting_player
        responding_players_card = self.stack[-1]

        if responding_players_card == starting_card or responding_players_card == 0:
            # responding_player has won
            self.winning = self.responding_player
        else:
            self.winning = self.starting_player

        self.notifier.notify("Player {} is winning after this round".format(self.winning.name))

    def playMatch(self):
        # play the first round
        self.notifier.notify("First round of this match!")

        self.stack.append(self.starting_player.playCardStarting())
        self.stack.append(self.responding_player.playCardResponding(self.stack))
        self.notifier.notifyCards(self.stack)

        # update winning status
        self.evaluateWinning()

        # now ask if the starting_player player wants a new round
        repeat_card = self.starting_player.playCardRepeating(self.stack, self.winning == self.starting_player)

        while repeat_card != None:
            # starting_player player has started a new round
            self.notifier.notify("New round of this match!")
            self.stack.append(repeat_card)
            self.stack.append(self.responding_player.playCardResponding(self.stack))
            self.notifier.notifyCards(self.stack)

            self.evaluateWinning()

            repeat_card = self.starting_player.playCardRepeating(self.stack, self.winning == self.starting_player)

        # end of match
        # the winning player should collect the cards from stack and add to his 'archive'
        self.notifier.notify("End of match..")

        self.winning.collectFromStack(self.stack)  # this also empties the stack

        for _player in [self.starting_player, self.responding_player]:
            self.notifier.notify("Player {} has {} points".format(_player.name, _player.score))

        return self.winning
