
def unique_styles(albums):
    s = []
    for i in albums:
        for j in i.split(","):
            s.append(j)
    return len(set(s))

