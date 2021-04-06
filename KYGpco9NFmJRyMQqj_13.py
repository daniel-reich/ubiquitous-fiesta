
def min_removals(txt1, txt2):
    x = set(txt1).symmetric_difference(set(txt2))
    return(len(x))

