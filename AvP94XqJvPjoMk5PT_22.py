
def unique_styles(albums):
    res = set()
    for w in albums:
        res.update(set(w.split(',')))
    return len(res)

