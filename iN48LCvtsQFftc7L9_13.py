
def findStartLetter(letter,grid):
    result = list()
    for i,row in enumerate(grid):
        for j,l in enumerate(row):
            if letter == l:
                result.append((i,j))
    return result
def findStringWords(startPos,length,grid):
    result = list()
    #up
    if startPos[0] - (length-1)>= 0:
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]-i][startPos[1]]
            word = word + nextLetter.lower()
        result.append(word)
    #down
    if startPos[0] + (length-1)<= 7:
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]+i][startPos[1]]
            word = word + nextLetter.lower()
        result.append(word)
    #right
    if startPos[1] + (length-1)<= 7:
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]][startPos[1]+i]
            word = word + nextLetter.lower()
        result.append(word)
    #left
    if startPos[1] - (length-1)>= 0:
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]][startPos[1]-i]
            word = word + nextLetter.lower()
        result.append(word)
    
     #up right
    if (startPos[0] - (length-1)>= 0) & (startPos[1] + (length-1)<= 7) :
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]-i][startPos[1]+i]
            word = word + nextLetter.lower()
        result.append(word)
    #down right
    if (startPos[0] + (length-1)<= 7) & (startPos[1] + (length-1)<= 7) :
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]+i][startPos[1]+i]
            word = word + nextLetter.lower()
        result.append(word)
        
    #up left
    if (startPos[0] - (length-1)>= 0) & (startPos[1] - (length-1)>= 0) :
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]-i][startPos[1]-i]
            word = word + nextLetter.lower()
        result.append(word)
        
    #down left
    if (startPos[0] + (length-1)<= 7) & (startPos[1] - (length-1)>= 0) :
        word = grid[startPos[0]][startPos[1]].lower()
        for i in range(1,length):
            nextLetter = grid[startPos[0]+i][startPos[1]-i]
            word = word + nextLetter.lower()
        result.append(word)
​
    
    return result
​
def findWord(word,grid):
    pos = findStartLetter(word[0].upper(),grid)
    lst = list()
    for i in pos:
        lst.extend(findStringWords(i,len(word),grid))
    if word in lst:
        return True
    else:
        return False
​
def findWords(words,grid):
    for word in words:
        if findWord(word,grid):
            continue
        else:
            return False
    return True 
​
def makeGrid(letters):
    lst = list()
    for i in range(0,8):
        row = list()
        for j in range(0,8):
            row.append(letters[i*8 + j])
        lst.append(row)
    return lst
​
def word_search(letters, words):
    grid = makeGrid(letters)
    return findWords(words,grid)

