
def unmix(txt):
    retVal = ""
​
    arrTxt = list(txt)
​
    for i in range(0, len(arrTxt), 2):
        if i < len(arrTxt) - 1:
            retVal += arrTxt[i+1] + arrTxt[i]
        else:
            retVal += arrTxt[i]
​
    return retVal

