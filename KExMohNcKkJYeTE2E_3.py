
def is_orthogonal(f, s):
    return not sum([(f[x]*s[x]) for x in range(len(f))])

