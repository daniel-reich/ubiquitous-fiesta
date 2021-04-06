
def intersection(h1, h2):
    return [{k:h[k] for k in set(h1).intersection(set(h2))} for h in [h1,h2]]

