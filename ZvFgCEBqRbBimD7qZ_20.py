
def bowling(pins):
    score = 0
    frame = 1
    throw = 0
    for index, _ in enumerate(pins):
        throw += 1
        if throw == 1 and pins[index] == 10:
            if index < len(pins) - 2:
                score = score + 10 + pins[index + 1] + pins[index + 2]
                throw = 0
                frame += 1
            else:
                throw = 0
                frame += 1
        elif throw == 2:
            if pins[index] + pins[index - 1] == 10:
                score = score + 10 + pins[index + 1]
                throw = 0
                frame += 1
            else:
                score = score + pins[index] + pins[index - 1]
                throw = 0
                frame += 1
    return score

