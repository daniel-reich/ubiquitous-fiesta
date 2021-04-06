
def schoty(frame):
    included = True
    count = 0
    sum = 0
    for i in range(len(frame)-1,-1,-1):
        for each in frame[i]:
            if each == "O" and included:
                count += 1
            elif each == "-":
                included = False
        included = True
        sum += count * 10 ** (len(frame)-(i+1))
        count = 0
    return sum

