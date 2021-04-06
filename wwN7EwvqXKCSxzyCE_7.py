
def reorder_digits(lst, direction):
    new_lst = []
    if direction == 'asc':
        for i in lst:
            i = list(str(i))
            i.sort()
            i = int("".join(i))
            new_lst.append(i)
        return new_lst
    elif direction == 'desc':
        for i in lst:
            i = list(str(i))
            i.sort()
            i = list(reversed(i))
            i = int("".join(i))
            new_lst.append(i)
        return new_lst

