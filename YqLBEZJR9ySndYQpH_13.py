
def staircase(n):
    lst = list()
    if n > 0:
        for i in range(n):
            str = (n - 1 - i) * "_" + (i + 1) * "#"
            lst.append(str)
    elif n < 0:
        for i in range(-n):
            str = i * "_" + (-n - i) * "#"
            lst.append(str)
    return "\n".join(lst)

