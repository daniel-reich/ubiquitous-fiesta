
def full_cycle(lst):
    n = len(lst)
    reached = [False] * n
    cur = 0
    reached[0] = True
    while True:
        cur = lst[cur]
        if not (0 <= cur < n):
            return False
        if reached[cur]:
            return all(reached)
        reached[cur] = True

