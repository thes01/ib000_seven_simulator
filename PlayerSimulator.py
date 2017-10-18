from Player import Player
from Helpers import translateCardsToCodes, translateCodesToCards

def simulateStartingCard(PlayerClass, cards: list):
    player = PlayerClass("Foo", [])
    player.hand_cards = translateCardsToCodes(cards)

    print(player.playCardStarting())