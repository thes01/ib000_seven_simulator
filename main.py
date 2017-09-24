# card generator

# card format : 7:0, 8:1, 9:2, 10:3, J:4, Q:5, K:6, A:7
from random import shuffle, randint
from Player import Player
from Match import Match

john_points = 0
nick_points = 0

for i in range(10000):
    deck = []

    for cardValue in range(8):
        for n in range(4):
            deck.append(cardValue)

    shuffle(deck)
    shuffle(deck)

    john = Player("John", deck)
    nick = Player("Nick", deck)

    player_order = (john, nick)

    while len(deck) + len(john.hand_cards) + len(nick.hand_cards) > 0:
        player_order[0].takeToFull(True)
        player_order[1].takeToFull(False)
        match = Match(*player_order)
        player_order = match.playMatch()

    john_points += john.score()
    nick_points += nick.score()

print("END OF ALL - John got {} points, Nick got {} points".format(john_points, nick_points))
