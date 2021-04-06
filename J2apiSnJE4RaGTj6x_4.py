
find_broken_keys = lambda c, m: sorted(list(set(x
   for x, y in zip(c, m) if x != y)), key=c.index)

