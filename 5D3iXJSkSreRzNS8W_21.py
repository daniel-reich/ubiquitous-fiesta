
def news_at_ten(txt, n):
    lst = []
    a = n + (len(txt) * 2) - len(txt)
    for i in range(len(txt) + n + 1):
        screen = ""
        e = 0
        for i in range(n + (len(txt) * 2) + 1):
            if i != a:
                screen += " "
            elif e < len(txt):
                screen += txt[e]
                e += 1
                a += 1
        lst.append(screen[len(txt):(len(txt) + n)])
        a -= (1 + e)
    return lst

