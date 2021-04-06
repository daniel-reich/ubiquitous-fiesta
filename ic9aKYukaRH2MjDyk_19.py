
def sort_by_last(txt):
    return ' '.join(sorted(txt.split(' '), key=lambda s: ord(s[-1])))

