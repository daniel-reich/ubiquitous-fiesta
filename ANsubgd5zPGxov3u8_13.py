
def initialize(names):
    res = []
    for s in names:
        first, last = s.split()
        res.append('{}. {}.'.format(first[0], last[0]))
    return res

