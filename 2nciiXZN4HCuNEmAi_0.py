
flatten = lambda r: sum((flatten(v) for v in r), []) if type(r) is list else [r]

