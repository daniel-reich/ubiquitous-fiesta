
def censor_string(txt, lst, char):
    txtLst = txt.split()
    returnStr = ''
    for word in txtLst:
        if word in lst:
            word = char * len(word)
        returnStr = returnStr + " " + word  
    return returnStr.strip()

