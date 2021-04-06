
def lychrel(n):
    cnt = 1
    if (len(str(n)) == 1) or list(str(n)) == list(str(n))[::-1]:
        return 0
    while cnt <= 500:
        num = int("".join(map(str, list(str(n))[::-1])))
        t = n + num
        if list(str(t)) == list(str(t))[::-1]:
            return cnt
        else:
            n = t
        cnt += 1
    return True

