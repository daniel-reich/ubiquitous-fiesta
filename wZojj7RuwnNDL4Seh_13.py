
def completely_filled(lst):
    return all(' ' not in x[1:-1] if len(lst)>2 else True for x in lst)

