
def num_of_sublists(lst):
    for sub in lst:
        if type(sub) == list:
            return len(lst)
        return 0

