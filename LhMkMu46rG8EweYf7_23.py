
def sort_by_letter(r):
    return sorted(r, key = lambda x: [i for i in x if i.isalpha()][0])

