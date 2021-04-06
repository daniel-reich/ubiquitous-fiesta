
intersection = lambda a, b: [{y: x[y] for y in set(a) & set(b)} for x in (a, b)]

