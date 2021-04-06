
def inverter(txt, type):
    splitTxt = txt.split(" ")
    if type == "P":
        index = len(splitTxt) - 1
        invertedTxt = ""
        while index >= 0:
            invertedTxt += splitTxt[index]
            if index != 0:
                invertedTxt += " "
            index-=1
        return invertedTxt.lower().capitalize()
    elif type == "W":
        wordIndex = 0
        invertedTxt = ""
        while wordIndex < len(splitTxt):
            characterIndex = len(splitTxt[wordIndex]) - 1
            while characterIndex >= 0:
                invertedTxt+=splitTxt[wordIndex][characterIndex]
                characterIndex-=1
            if wordIndex != len(splitTxt) - 1:
                invertedTxt+=" "
            wordIndex+=1
        return invertedTxt.lower().capitalize()

