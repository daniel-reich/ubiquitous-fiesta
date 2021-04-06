
def ascending(inp):
​
    def is_ascending(list_of_strs):
        for s1, s2 in zip(list_of_strs, list_of_strs[1:]):
            if int(s2) - int(s1) is not 1:
                return False
        return True
​
    L = len(inp)
​
    for n in range(1, L):
        if L % n != 0:
            continue
        possible_numbers = [inp[i:i + n] for i in range(0, L, n)]
        if is_ascending(possible_numbers):
            return True
    return False

