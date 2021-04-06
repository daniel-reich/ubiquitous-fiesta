
def tidy_books(lst):
    return [x.strip().split(' - ') for txt in lst for x in txt]

