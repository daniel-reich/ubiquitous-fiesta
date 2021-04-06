
def jazzify(lst):
    return [c if c[-1] == '7' else c + '7' for c in lst]

