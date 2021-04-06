
def tidy_books(lst):
    l = []
    for book in lst:
        for b in book:
            t, a = b.split('-')
            l.append([t.strip(), a.strip()])      
    return l

