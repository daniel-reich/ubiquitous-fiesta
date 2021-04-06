
def min_swaps(string):
    aim1 = "".join(str(x % 2) for x in range(len(string)))
    aim2 = "".join(str((x + 1) % 2) for x in range(len(string)))
    if string == aim1 or string == aim2:
        return 0
    aim1 = sum(x == y for x, y in zip(string, aim1))
    aim2 = sum(x == y for x, y in zip(string, aim2))
    return min(aim1, aim2)

