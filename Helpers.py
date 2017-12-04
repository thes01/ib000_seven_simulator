from random import shuffle

def assessCards(cards):
    """ iterate through cards and return number of points in there"""
    score = 0
    for card in cards:
        if card == 3 or card == 7:
            score += 1
    return score

def translateCardsToCodes(cards):
    """ 'translate' human-readable card values to its code variants """
    translate_table = ["7", "8", "9", "10", "J", "Q", "K", "A"]
    return list(map(lambda card: translate_table.index(card), cards))

def translateCodesToCards(codes):
    return list(map(translateCodeToCard, codes))

def translateCodeToCard(code):
    translate_table = ["7", "8", "9", "10", "J", "Q", "K", "A"]
    return translate_table[code]

def isValuableCard(card):
    return card == 3 or card == 7

def generateNewRandomDeck(deck: list):
    deck.clear()
    deck.extend([0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7])
    shuffle(deck)