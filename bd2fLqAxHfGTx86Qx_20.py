
def can_complete(initial, word):
    i = 0
    for c in word:
        if c == initial[i]:
            i += 1
            if i == len(initial):
                return True
    return False

