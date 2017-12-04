from Player import Player
from Helpers import *
from Notifier import Notifier
from Match import Match

class Tournament():
    def __init__(self, player1: Player, player2: Player, n_games: int):
        if n_games % 2 == 0:
            raise ValueError("Error: number of games in tournament must be an odd number!")

        # initialize an empty deck and join to the players
        self.deck = []
        player1.deck = self.deck
        player2.deck = self.deck

        self.player1 = player1
        self.player2 = player2
        self.starting_player = player1
        self.n_games = n_games

        self.player1_stats = {
            'games_won' : 0,
            'total_points' : 0
        }

        self.player2_stats = {
            'games_won' : 0,
            'total_points' : 0
        }

        self.notifier = Notifier()

    @property
    def responding_player(self):
        return self.player1 if self.starting_player == self.player2 else self.player2

    def playTournament(self):
        for game in range(self.n_games):
            generateNewRandomDeck(self.deck)

            # count total cards available
            while len(self.deck) + len(self.player1.hand_cards) + len(self.player2.hand_cards) > 0:
                self.starting_player.takeToFull(True)
                self.responding_player.takeToFull(False)
                match = Match(self.starting_player, self.responding_player)
                # the next starting player will be the one who has won current match
                self.starting_player = match.playMatch()

            # the last starting player is the one who won the final match, so he gets 1 extra point
            self.starting_player.score += 1

            if self.player1.score > self.player2.score:
                self.player1_stats['games_won'] += 1
                self.notifier.notify("End of game No.{} Player {} has won with {} points".format(
                    game+1, self.player1.name, self.player1.score
                ))
            else:
                self.player2_stats['games_won'] += 1
                self.notifier.notify("End of game No.{} Player {} has won with {} points".format(
                    game+1, self.player2.name, self.player2.score
                ))

            self.player1_stats['total_points'] += self.player1.score
            self.player2_stats['total_points'] += self.player2.score

            self.player1.endOfGame()
            self.player2.endOfGame()

    def getAbsoluteWinner(self):
        if self.player1_stats['games_won'] > self.player2_stats['games_won']:
            return self.player1
        else:
            return self.player2