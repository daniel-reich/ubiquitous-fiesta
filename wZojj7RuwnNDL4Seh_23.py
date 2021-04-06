
def completely_filled(lst):
    return all(' ' not in j for i in lst for j in i)

