
def soroban(frame):
    upperDeck = ["0" for each in range(0, 7)]
    lowerDeck = ["0" for each in range(0, 7)]
    index = 0
    
    #UPPER DECK
    while index < len(frame[0]):
        if frame[0][index] == "|":
            upperDeck[index] = "5"
        index+=1
    
    #LOWER DECK
    lowerFrame = frame[3:]
    rowIndex = 0
    while rowIndex < len(lowerFrame):
        colIndex = 0
        while colIndex < len(lowerFrame[rowIndex]):
            if lowerFrame[rowIndex][colIndex] == "|":
                lowerDeck[colIndex] = str(rowIndex)
            colIndex +=1
        rowIndex+=1
    
    upperString = ""
    lowerString = ""
    
    deckIndex = 0
    while deckIndex < len(upperDeck):
        upperString += upperDeck[deckIndex]
        lowerString += lowerDeck[deckIndex]
        deckIndex+=1
    
    return int(upperString)+int(lowerString)

