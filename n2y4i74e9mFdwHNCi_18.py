
def get_items_at(arr, par):
    if len(arr) == 0:
        return []
    indx = len(arr)-1
    position = 1
    return get_items(arr, par, indx, position)
​
def get_items(arr, par, indx, position):
    if indx == 0:
        if parity(par, position):
            return arr
        else:
            del arr[indx]
            return arr
    if not parity(par, position):
        del arr[indx]
    return get_items(arr, par, indx-1, position+1)
​
def parity(par, position):
    if par == 'odd' and position % 2 == 1:
        return True
    elif par == 'even' and position % 2 == 0:
        return True
    else:
        return False

