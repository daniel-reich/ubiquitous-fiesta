
def rotate_by_one(lst):
    last_el = lst.pop()
    lst.insert(0, last_el)
    return lst

