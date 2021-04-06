
def isWordChain(words):
​
    for i in range(len(words)-1):
        if len(words[i]) == len(words[i+1]):
            if 1 != sum(1 if words[i][x] != words[i+1][x] else 0 for x in range(len(words[i]))):
                return False
        elif len(words[i]) == len(words[i+1]) + 1:
            if 1 < sum(1 if words[i][x] not in words[i+1] else 0 for x in range(len(words[i]))):
                return False
        elif len(words[i]) + 1 == len(words[i+1]):
            if 1 < sum(1 if words[i+1][x] not in words[i] else 0 for x in range(len(words[i+1]))):
                return False
        else:
            return False
    return True

