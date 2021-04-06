
def mumbling(s):
    return '-'.join((l * (idx + 1)).title() for idx, l in enumerate(s))

