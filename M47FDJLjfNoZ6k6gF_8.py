
def cup_swapping(swaps):
    cup = 'B'
​
    for i in range(len(swaps)):
        if cup == swaps[i][0]:
            cup = swaps[i][1]
        elif cup == swaps[i][1]:
            cup = swaps[i][0]
    return cup

