
alph = 'abcdefgh'
import math
lst = []
for i in range(8):
    for a in range(8):
        lst.append(alph[a] + str(i + 1))
#print(lst)
​
refDict = {}
for a in lst:
    
    refDict[a] = ( alph.index(a[0]) , int(a[1]) )  
​
​
#Move towards
#Check distance
​
def getReachable(pos):
    out = []
    posX = refDict[pos][0]
    posY = refDict[pos][1]
    for key in refDict.keys():
        if key == pos:
            continue
        x = refDict[key][0]
        y = refDict[key][1]
        if (posX - x) == 0:
            continue
        slope = (posY - y) / (posX - x)
​
        if slope == 1 or slope == -1:
            out.append(key)
    return out
​
def closest(start, end):
    startX = refDict[start][0]
    startY = refDict[start][1]
    endX = refDict[end][0]
    endY = refDict[end][1]
    
    distances = {}
​
    for pos in getReachable(start):
        pX = refDict[pos][0]
        pY = refDict[pos][1]
        if pX == startX and pY == startY:
            return pos
        dist = math.sqrt( (pX - endX) ** 2 + (pY - endY) ** 2 )
        distances[pos] = dist
​
    for key in distances.keys():
        if distances[key] == min(distances.values()):
            #print(distances)
            return key
​
#Returns true if it forms a     #
                              # X #
                                #
def isImpossible(start, end):
    start = refDict[start]
    end = refDict[end]
​
    startX, startY = start[0], start[1]
    endX, endY = end[0], end[1]
​
    if startX == endX and abs(startY - endY) == 1:
        return True
    if startY == endY and abs(startX - endX) == 1:
        return True
    return False
​
def bishop(start, end, num):
  if start == end:
    return True
  close = closest(start, end)
  i = 0
  while i < num:
​
​
    if close == end:
      return True
    if isImpossible(close, end):
      return False
    else:
      close = closest(close, end)
    i = i + 1
  return False

