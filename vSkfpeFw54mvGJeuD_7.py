
def lychrel(n):
    cnt = 0
    while True:
        if str(n) == str(n)[::-1]:
            return cnt
        cnt += 1
        if cnt > 500:
            return True
        n += int(str(n)[::-1])

