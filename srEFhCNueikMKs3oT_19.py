
def consecutive_sum(n):
    n2 = 2 * n
    for diff in range(1, n + 1):
        if not n2 % (diff + 1):
            start2 = n2 // (diff + 1) - diff
            if not start2 % 2 and 0 < start2 // 2 < n:
                return True
    return False

