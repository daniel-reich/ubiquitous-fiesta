
def bowling(pins):
    total = 0
    throw = 0
    frame = 1
    while throw < len(pins):
        count = 1
        if count == 1:
            if pins[throw] == 10:
                #strike
                bonus = 'strike'
                if frame == 10:
                    total += 10 + pins[throw+1] + pins[throw+2]
                    break
                else:
                    try:
                        total += 10 + pins[throw+1] + pins[throw+2]
                    except:
                        try:
                            total += 10 + pins[throw+1]
                        except:
                            total += 10
                throw += 1
                frame += 1
            else:
                count += 1
                throw += 1
​
        if count == 2:
            if throw == len(pins):
                total += pins[throw-1]
            else:
                if pins[throw] + pins[throw-1] == 10:
                    #spare
                    bonus = 'spare'
                    if frame == 10:
                        total += 10 + pins[throw+1]
                        break
                    else:
                        try:
                            total += 10 + pins[throw+1]
                        except:
                            total += 10
                    throw += 1
                    frame += 1
                else:
                    #simple add
                    bonus = ''
                    total += pins[throw] + pins[throw-1]
                    throw += 1
                    frame += 1
    return total

