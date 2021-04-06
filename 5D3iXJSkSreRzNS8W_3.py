
def news_at_ten(txt, n):
    s = " " * n + txt + " " * n
    return [s[i: i + n] for i in range(n + len(txt) + 1)]

