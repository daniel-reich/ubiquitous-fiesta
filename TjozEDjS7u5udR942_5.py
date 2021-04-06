
def sort_authors(lst):
    return sorted(lst, key=lambda name: name.split()[-1][0].lower())

