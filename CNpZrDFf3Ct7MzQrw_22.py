
def trouble(num1, num2):
    trips = []
    doubs = []
    for i in range(len(str(num1))-2):
        if str(num1)[i] == str(num1)[i+1] and str(num1)[i] == str(num1)[i+2]:
            trips += [str(num1)[i]]
    for j in range(len(str(num2))-1):
        if str(num2)[j] == str(num2)[j + 1]:
            doubs += [str(num2)[j]]
    out = False
    for each in trips:
        if each in doubs:
            out = True
    return out

