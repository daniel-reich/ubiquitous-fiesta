
def min_removals(txt1, txt2):
    return(sum([1 for x in txt1 if x not in txt2]) + sum([1 for y in txt2 if y not in txt1]))

