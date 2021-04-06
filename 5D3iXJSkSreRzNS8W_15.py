
def news_at_ten(txt, n):
    return(list(map(lambda i: (' '*n + txt + ' '*n)[i:i + n], range(n + len(txt) + 1))))

