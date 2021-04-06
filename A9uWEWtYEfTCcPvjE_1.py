
from itertools import permutations
def price_importance_sort(dct, b):
    amounts, newGroup, listImportance = {}, [], {}
    groups = list(permutations(range(len(dct))))
    for i in groups:
        newPrice, newGroup = 0, []
        for j in i:
            newPrice+=dct[list(dct)[j]]["price"]
            newGroup.append(j)
            if (i.index(j)!=(len(i)-1) and newPrice+i[i.index(j)+1]>b and newPrice<=b):
                amounts.update({''.join(map(str, newGroup)):newPrice})
                continue
    for i in amounts:
        importanceVals = 0
        for j in i:
            importanceVals+=dct[list(dct)[int(j)]]["importance"]
        listImportance.update({i:importanceVals})
    theGroup = max(listImportance.values())
    for code, imp in listImportance.items():
        if imp == theGroup: theGroup=code
    totals = []
    for i in theGroup: totals.append(list(dct)[int(i)])
    return sorted(totals)

