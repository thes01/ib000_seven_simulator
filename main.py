# card generator

# card format : 7:0, 8:1, 9:2, 10:3, J:4, Q:5, K:6, A:7
from random import shuffle, randint
from Player import Player
from Match import Match

deck = []

for cardValue in range(8):
    for n in range(4):
        deck.append(cardValue)

shuffle(deck)
shuffle(deck)

john = Player("John", deck)
nick = Player("Nick", deck)

# john.takeToFull(True)
# nick.takeToFull(False)

player_order = (john, nick)

while len(deck) + len(john.hand_cards) + len(nick.hand_cards) > 0:
    player_order[0].takeToFull(True)
    player_order[1].takeToFull(False)
    match = Match(*player_order)
    player_order = match.playMatch()

# print(john.score())
# print(nick.score())