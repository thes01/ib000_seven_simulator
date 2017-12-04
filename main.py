# card generator

# card format : 7:0, 8:1, 9:2, 10:3, J:4, Q:5, K:6, A:7
from Player import Player
from OtherPlayers import *
from Notifier import Notifier
from Tournament import Tournament

N_TOTAL_TOURNAMENTS = 200
N_GAMES_IN_TOURNAMENT = 11

# global settings for notify module, 0 = no messages, 2 = all messages
Notifier.notify_level = 0

first = SensiblePlayer("Zacinajici hrac")
second = SensiblePlayer("Odpovidajici hrac")

with open('output_t.csv', 'a') as output:
    #generate possible 4-tuples for all value combinations 0-4, 0-4, 0-4, True/False
    combinations = [(a, b, c, d) for a in range(4, 5) for b in range(5) for c in range(5) for d in range(2)]

    for combination in combinations:
        second.VALUABLE_STARTING_MIN_REPEATABILITY = combination[0]
        second.VALUABLE_RESPONDING_MIN_REPEATABILITY = combination[1]
        second.MIN_STACK_VALUE_TO_REPEAT = combination[2]
        second.IGNORE_WINNING_WHEN_REPEATING = combination[3] == 1

        # total statistics
        n_first_won_tournaments = 0
        n_first_won_games = 0

        # play as many tournaments as needed
        for TOURNAMENT in range(N_TOTAL_TOURNAMENTS):
            tournament = Tournament(first, second, N_GAMES_IN_TOURNAMENT)
            tournament.playTournament()

            if tournament.getAbsoluteWinner() == first:
                n_first_won_tournaments += 1

            n_first_won_games += tournament.player1_stats['games_won'] 

        # statistics: (combination) : average percentage of games won in tournament
        print("Combination {} : {}".format(combination, 100*((n_first_won_games / N_TOTAL_TOURNAMENTS)/N_GAMES_IN_TOURNAMENT)))
        output.write('{};{};{};{};{}\n'.format(combination[0], combination[1], combination[2], combination[3], 100*((n_first_won_games / N_TOTAL_TOURNAMENTS)/N_GAMES_IN_TOURNAMENT)).replace('.', ','))