
def cup_swapping(swaps):
    ball = "B"
    for move in swaps:
        if ball in move:
            ball = move[1] if move[0] == ball else move[0]
    return ball

