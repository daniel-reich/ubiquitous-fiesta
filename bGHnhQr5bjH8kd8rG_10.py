
def rotate_by_one(lst):
    length = len(lst)
    num = lst[length-1]
    lst.insert(0, num)
    lst.pop(length)
    return lst

