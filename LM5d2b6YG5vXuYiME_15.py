
def can_enter_cave(listString):
    listMaze = listString
​
    for i in range(len(listMaze[0]) - 1):
        canStep = False
        for j in range(len(listMaze)):
            if listMaze[j][i] + listMaze[j][i + 1] == 0:
                canStep = True
            
        if canStep == False:
            break
​
    return canStep

