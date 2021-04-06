
def complete_pattern(s):
    repeats = []
    for i in set(s):
        new = s[:].replace('_', i)
        for j in range(1, len(s) + 1):
            if (new[:j]*(len(s)//j + 1))[:len(s)] == new:
                repeats.append((j, i))
    return min(repeats)[1]

