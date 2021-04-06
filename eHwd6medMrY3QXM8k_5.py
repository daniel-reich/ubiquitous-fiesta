
def is_consecutive(s):
    size = len(s)
    for i in range(1, size//2 + 1):
        if size%i == 0:
            groups = [int(s[j:j+i]) for j in range(0, size, i)]
            diff = [b - a for a, b in zip(groups, groups[1:])]
            if set(diff) in ({1}, {-1}):
                return True
    return False

