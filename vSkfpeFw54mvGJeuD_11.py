
def lychrel(n):
    if str(n) == str(n)[::-1]:
        return 0
    for i in range(1,501):
        n = int(str(n)[::-1]) + int(n)
        if str(n) == str(n)[::-1]:
            return i
    else:
        return True

