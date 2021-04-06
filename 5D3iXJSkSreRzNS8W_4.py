
def news_at_ten(txt, n):
    line = ' ' * n + txt + ' ' * n
    return [line[i:i+n] for i in range(n + len(txt) + 1)]

