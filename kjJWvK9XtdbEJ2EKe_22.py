
def sort_array(lst):
    return [lst.pop(lst.index(min(lst))) for x in range(len(lst))]

