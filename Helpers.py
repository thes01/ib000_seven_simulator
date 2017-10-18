from random import shuffle

def assessCards(cards):
    score = 0
    # iterate through cards and count points from 10s and As - each for 1 point
    for card in cards:
        if card == 3 or card == 7:
            score += 1
    return score

def translateCardsToCodes(cards):
    translate_table = ["7", "8", "9", "10", "J", "Q", "K", "A"]

    return list(map(lambda card: translate_table.index(card), cards))

def translateCodesToCards(codes):
    translate_table = ["7", "8", "9", "10", "J", "Q", "K", "A"]

    return list(map(lambda code: translate_table[code], codes))

def isValuableCard(card):
    return card == "3" or card == "7";

def generateRandomDeck(deck: list):
    deck.clear()

    for cardValue in range(8):
        for n in range(4):
            deck.append(cardValue)

    shuffle(deck)
    shuffle(deck)

def gameConsole()