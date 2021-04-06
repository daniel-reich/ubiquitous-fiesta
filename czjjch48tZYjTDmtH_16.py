
def is_shifted(lst1, lst2):
    zippedItems = list(zip(lst1, lst2))
    shiftKey = zippedItems[0][1]-zippedItems[0][0]
    for item, shiftItem in zippedItems:
        result = item + shiftKey
        if not result == shiftItem:
            return False
    return True
​
def is_multiplied(lst1, lst2):
    zippedItems = list(zip(lst1, lst2))
    shiftKey = zippedItems[0][1] / zippedItems[0][0]
    for item, shiftItem in zippedItems:
        result = item * shiftKey
        if not result == shiftItem:
            return False
    return True

