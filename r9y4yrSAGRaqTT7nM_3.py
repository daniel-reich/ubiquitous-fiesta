
def find_missing(l):
    if not l: #Check if l is None
        return False
​
    subLstLengths = sorted([len(i) for i in l])
​
    if not all(subLstLengths): #Check if l contains []
        return False
​
    for x in range(min(subLstLengths),max(subLstLengths)+1):
        if x not in subLstLengths:
            return x

