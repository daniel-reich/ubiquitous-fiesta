
def cup_swapping(swaps):
    initial = "B"
    for ball in swaps:
        if initial in ball:initial = ball.replace(initial,"")
    return initial

