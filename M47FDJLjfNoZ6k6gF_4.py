
def cup_swapping(swaps):
    pos = {chr(65+k): k for k in range(3)}
    for swap in swaps:
        cup1, cup2 = swap[0], swap[1]
        pos[cup1], pos[cup2] = pos[cup2], pos[cup1]
    for cup, p in pos.items():
        if p == 1:
            return cup

