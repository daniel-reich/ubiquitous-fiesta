
def duplicate_count(txt):
    return sum([1 for x in set(txt) if txt.count(x) > 1])

