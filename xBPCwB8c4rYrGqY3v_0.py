
def missing(lst):
    increment = (max(lst) - min(lst))/len(lst)
    for i in lst:
        if i + increment not in lst:
            return i + increment

