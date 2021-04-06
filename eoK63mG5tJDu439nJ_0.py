
def isWordChain(words):
    for x, y in zip(words, words[1:]):
        if len(x) == len(y) and sum(1 for i in x if i not in y) == 1:
            continue
        elif len(x) + 1 == len(y) and sum(1 for i in x if i not in y) == 0:
            continue
        elif len(y) + 1 == len(x) and sum(1 for i in y if i not in x) == 0:
            continue
        else:
            return False
    return True

