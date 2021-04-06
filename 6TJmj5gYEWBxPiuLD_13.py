
def seating_students(lst):
    ways = 0
    n = lst.pop(0)
    for s1 in range(1, n + 1):
        if s1 in lst:
            continue
        if s1 < n - 1 and s1 + 2 not in lst:
            ways += 1
        if s1 % 2 == 1 and s1 < n and s1 + 1 not in lst:
            ways += 1
    return ways

