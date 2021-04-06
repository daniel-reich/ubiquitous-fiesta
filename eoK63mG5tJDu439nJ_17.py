
def isWordChain(words):
    for i in range(1, len(words)):
        if abs(len(words[i]) - len(words[i - 1])) > 1:
            return False
        if len(words[i - 1]) == len(words[i]):
            for j in range(len(words[i - 1])):
                if words[i - 1][j] != words[i][j]:
                    if words[i - 1][:j] + words[i - 1][j + 1:] != \
                            words[i][:j] + words[i][j + 1:]:
                        return False
        else:
            if len(words[i - 1]) > len(words[i]):
                bigger, smaller = words[i - 1], words[i]
            else:
                bigger, smaller = words[i], words[i - 1]
            for j in range(len(bigger)):
                if bigger[j] not in smaller:
                    if bigger[:j] + bigger[j + 1:] != smaller:
                        return False
    return True

