
def move_zeros(lst):
    lst = [elem if type(elem) != bool else True for elem in lst]
    remove_zeros, add_zeros = lst.count(0), lst.count(0)
    while remove_zeros > 0:
        lst.remove(0)
        remove_zeros -= 1
    while add_zeros > 0:
        lst.append(0)
        add_zeros -= 1
    return [elem if type(elem) != bool else False for elem in lst]

