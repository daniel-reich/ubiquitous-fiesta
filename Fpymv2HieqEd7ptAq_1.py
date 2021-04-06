
def split(txt):
    clusters = []
    group = ''
    n = 0
​
    for i in txt:
        group += i
        n = n + 1 if i == '(' else n - 1
        if n == 0:
            clusters.append(group)
            group = ''
​
    return clusters

