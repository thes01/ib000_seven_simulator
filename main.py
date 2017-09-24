# card generator

# card format : 7:0, 8:1, 9:2, 10:3, J:4, Q:5, K:6, A:7
from random import shuffle, randint
from Player import Player

deck = []

for cardValue in range(8):
    for n in range(4):
        deck.append(cardValue)

shuffle(deck)
shuffle(deck)

john = BadPlayer("John", deck)
nick = BetterPlayer("Nick", deck)

john.takeToFull(True)
nick.takeToFull(False)

while len(deck) > 0:
    round = randint(1, 4)
    john.playNCards(round)
    nick.playNCards(round)
    john.takeToFull(True)
    nick.takeToFull(False)

print(john.score())
print(nick.score())