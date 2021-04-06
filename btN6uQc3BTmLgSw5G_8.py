
def findSpiralPoint(num):
    return (num-1) // 2
    
def makeStrReady(num, string):
    shouldBe = num*num
    if len(string) == shouldBe:
        return string
    if len(string) > shouldBe:
        return string[:shouldBe]
    if len(string) < shouldBe:
        while len(string) != shouldBe:
            string += "+"
        return string
        
def isValidBox(curr, num, res):
    return res[curr[0]][curr[1]] == 0 and curr[0] != -1 and curr[1] != -1 and curr[0] != num and curr[1] != num
    
def move(direction, curr):
    if direction == "R":
        return (curr[0], curr[1]+1)
    elif direction == "D":
        return (curr[0]+1, curr[1])
    elif direction == "L":
        return (curr[0], curr[1]-1)
    elif direction == "U":
        return (curr[0]-1, curr[1])
​
def spiral_matrix(num, string):
    result = []
    for i in range (num):
        result.append([0]*num)
    string = makeStrReady(num, string)
    mid = findSpiralPoint(num)
    result[mid][mid] = string[0]
    curr = (mid, mid)
    nextMove = "R"
    for char in string[1:]:
        if nextMove == "R":
            nextB = (curr[0], curr[1]+1)
            if isValidBox(nextB, num, result):
                result[nextB[0]][nextB[1]] = char
                curr = nextB
                nextMove = "D"
            else:
                nextB = move("U", curr)
                result[nextB[0]][nextB[1]] = char
                curr = nextB
                nextMove = "R"
                
        elif nextMove == "D":
            nextB = (curr[0]+1, curr[1])
            if isValidBox(nextB, num, result):
                result[nextB[0]][nextB[1]] = char
                curr = nextB
                nextMove = "L"
            else:
                nextB = move("R", curr)
                result[nextB[0]][nextB[1]] = char
                curr = nextB
                nextMove = "D"
                
        elif nextMove == "L":
            nextB = (curr[0], curr[1]-1)
            if isValidBox(nextB, num, result):
                result[nextB[0]][nextB[1]] = char
                curr = nextB
                nextMove = "U"
            else:
                nextB = move("D", curr)
                result[nextB[0]][nextB[1]] = char
                curr = nextB
                nextMove = "L"
                
        elif nextMove == "U":
            nextB = (curr[0]-1, curr[1])
            if isValidBox(nextB, num, result):
                result[nextB[0]][nextB[1]] = char
                curr = nextB
                nextMove = "R"
            else:
                nextB = move("L", curr)
                result[nextB[0]][nextB[1]] = char
                curr = nextB
                nextMove = "U"
                
    return result

