
def replace_next_largest(lst):
    indeces = sorted(range(len(lst)), key=lst.__getitem__)
    return [v for _,v in sorted(zip(indeces, sorted(lst)[1:]+[-1]))]

