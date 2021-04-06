
def discount(n, txt):
    if txt == '': return n
    for disc in sorted((1, -float(d[:-1])) if d[-1] == '%' else (2, -float(d)) for d in txt.split(', ')):
        if disc[0] == 1:
            n += n * disc[1] / 100
        else:
            n += disc[1]
    return round(n, 2)

