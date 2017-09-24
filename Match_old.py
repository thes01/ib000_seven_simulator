
def evaluateWinning(stack):
    first = stack[-2]
    second = stack[-1]

    if (first == second or second == 0)
        print("Second is now winning")
        return 1
    
    print("First is now winning")
    return 0

def playMatch(first, second):
    winning_player = first
    stack = []

    # play the first round
    stack.append(first.playCardStarting())
    stack.append(second.playCardResponding(stack))

    print("Stack: {}".format(stack))
    # update winning status
    winning_player = evaluateWinning(stack, first, second)

    repeat_card = first.playCardRepeating(stack, winning_player == first)

    while repeat_card is not None:
        # first player has started a new round
        stack.append(repeat_card)
        stack.append(second.playCardResponding(stack))

        winning_player = evaluateWinning(stack, first, second)

        repeat_card = first.playCardRepeating(stack, winning_player == first)

    # the winning player should collect the cards from stack and add to his 'archive'

    
    # match is done
    if (winning_player == 0):
        return (first, second)
    else:
        return (second, first)