def assessCards(cards):
    score = 0
    # iterate through current archive cards and count 10s and As - each for 1 point
    for card in cards:
        if card == 3 or card == 7:
            score += 1
    return score

def printCards(cards):
    translate_table = ["7", "8", "9", "10", "J", "Q", "K", "A"]
    message = "Stack: "

    for card_code in cards:
        message += translate_table[card_code] + ", "

    print(message[:-2]) # cut the ending comma and space

def translateCardsToCodes(cards):
    translate_table = ["7", "8", "9", "10", "J", "Q", "K", "A"]

    return list(map(lambda card: translate_table.index(card), cards))

def translateCodesToCards(codes):
    translate_table = ["7", "8", "9", "10", "J", "Q", "K", "A"]

    return list(map(lambda code: translate_table[code], codes))