
def sort_array(lst):
    sorted_list = []
    while lst:
        m = min(lst)
        sorted_list.append(m)
        lst.remove(m)
    return sorted_list

