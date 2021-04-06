
def high_low(txt):
    txt = list(map(int, txt.split(" ")))  
    minNum = min(txt)
    maxNum = max(txt)
    return str(maxNum) + " " + str(minNum)

