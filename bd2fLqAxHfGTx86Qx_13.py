
def can_complete(initial, word):
    begin = 0
    for c in initial:
        if c in word[begin:]:
            begin += word[begin:].index(c) + 1
        else:
            return False
    return True

