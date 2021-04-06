
def order(lst):
    return [tup[0] for tup in sorted(list(zip(list(range(len(lst))), lst)), key=lambda x: x[1])]

