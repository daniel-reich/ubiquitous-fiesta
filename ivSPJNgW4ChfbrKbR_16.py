
top = {
    "O|": 0,
    "|O": 5
}
bottom = {
    "|OOOO": 0,
    "O|OOO": 1,
    "OO|OO": 2,
    "OOO|O": 3,
    "OOOO|": 4
}
​
def splitList(array, charToSplit):
    indexSplit = array.index(charToSplit)
    bef = []
    aft = []
​
    for i in range(0, indexSplit):
        bef.append(array[i])
​
    for j in range(indexSplit + 1, len(array)):
        aft.append(array[j])
​
    return [top["".join(bef)], bottom["".join(aft)]]
​
​
def getSorobanDesign(soroban):
    ans = []
    num = soroban[0]
    for i in range(0, len(num)):
        ans.append([])
​
    for line in soroban:
        for i in range(0, len(line)):
            ans[i].append(line[i])
​
    for array in ans:
        ans[ans.index(array)] = splitList(array, "-")
​
    return ans
​
def soroban(design):
    array = getSorobanDesign(design)
    preAnswer = ""
    for _list in array:
        preAnswer += str(_list[0] + _list[1])
​
    answer = int(preAnswer)
    return answer

