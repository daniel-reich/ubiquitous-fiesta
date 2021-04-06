
def consecutive_sum(n):
    for i in range(1, n-1):
        tot = i
        while True:
            i += 1
            tot += i
            if tot == n:
                return True
            if tot > n:
                break
    return False

