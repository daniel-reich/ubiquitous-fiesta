
def rotate_by_one(lst):
    last_element = lst[-1]
    lst.insert(0, last_element)
    lst.pop()
    return lst

