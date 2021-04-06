
def sort_array(lst):
    return [x for x in list(range(sum(lst)*-1,sum(lst)+1)) if x in lst]

