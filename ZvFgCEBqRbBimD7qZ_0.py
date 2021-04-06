
def bowling(pins):
    frame, score = 1, 0
    while frame < 10:
        if pins[0] == 10:
            score += sum(pins[:3])
            pins = pins[1:]
        elif sum(pins[:2]) == 10:
            score += sum(pins[:3])
            pins = pins[2:]
        else:
            score += sum(pins[:2])
            pins = pins[2:]
        frame += 1
    return score + sum(pins)

