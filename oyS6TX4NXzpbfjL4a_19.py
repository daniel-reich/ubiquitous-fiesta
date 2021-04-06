
def best_start(lst, word):
​
    d = {
        'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G': 2, 'H':4, 'I':1, 'J':8,
        'K':5, 'L':2, 'M':3, 'N':1, 'O':1, 'P':3, 'Q': 10, 'R':1, 'S':1, 'T':1,
        'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10
        }
​
​
    lenWd = len(word)
    lenLs = len(lst)
    scoreList = []
    for ind in range(lenLs):
        if((ind + lenWd) > lenLs): break
​
        pat = lst[ind : ind + lenWd]
        mult = 1
        score = 0
        for indPat in range(len(pat)):
            val = d[word[indPat].upper()]
            if(pat[indPat] == 'DL'):
               val *= 2
            elif(pat[indPat] == 'TL'):
               val *= 3
            elif(pat[indPat] == 'DW'):
               mult = 2
               
            score += val
        scoreList.append(score * mult)
​
    maxInd = 0
    maxVal = scoreList[0]
    for i in range(1, len(scoreList)):
        if(scoreList[i] > maxVal):
            maxVal = scoreList[i]
            maxInd = i
​
    return maxInd

