
def id_mtrx(n):
    if isinstance(n, str):
        return "Error"
    ol = []
    num = abs(n)
    for i in range(num):
        il = []
        for j in range(num):
            if i == j:
                il.append(1)
            else:
                il.append(0)
        ol.append(il)
    return ol if n > 0 else ol[::-1]

