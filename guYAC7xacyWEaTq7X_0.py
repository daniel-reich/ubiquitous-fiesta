
def is_autobiographical(n):
    s = str(n)
    return all(s.count(str(idx)) == int(i) for idx, i in enumerate(s))

