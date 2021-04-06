
def bowling(pins):
    total = 0
    frame = 0
    newframe = True
    for index, pin in enumerate(pins):
        if frame == 10:
            break
        if pin == 10 and newframe:
            total += pins[index+1]
            total += pins[index+2]
            frame += 1
        elif not newframe:
            if pins[index - 1] + pin == 10:
                total += pins[index+1]
            frame += 1
            newframe = True
        else:
            newframe = False
        total += pin
    return total

