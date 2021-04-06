
def paul_cipher(txt):
    alphabets = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    textList = [t.upper() for t in txt]
    print(textList)
    print(textList)
    finalString = []
    index = 0
    for i in range(0, len(textList)):
        current = textList[i]
        if current.isdigit() == True:
            finalString.append(current)
        elif current.isalpha() == True:
            currentIndex = alphabets.index(current) + index
            index = alphabets.index(textList[i]) + 1
            if currentIndex >= 26:
                currentIndex -= 26
                finalString.append(alphabets[currentIndex])
            else:
                finalString.append(alphabets[currentIndex])
        else: 
            finalString.append(current)
    return "".join(finalString)

