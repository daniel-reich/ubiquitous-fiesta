
def max_separator(txt):
    diff = sorted([(txt.find(c, i+1) - i, c) for i, c in enumerate(txt)])
    return [e for n, e in diff if n > 0 and max(diff)[0] == n]

