
def min_length(lst: list, n: int) -> int:
    if max(lst) > n:
        return 1
    j = 2
    while True:
        for i in range(len(lst) - j + 1):
            if sum(lst[i:i+j]) > n:
                return j
        j += 1
        if j == len(lst):
            if sum(lst) > n:
                return j
            return -1

