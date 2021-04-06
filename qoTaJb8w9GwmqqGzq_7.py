
def is_subset(lst1, lst2):
    count = 0
    for i in lst1:
        if i in lst2:
            count += 1
    if count == len(lst1):
        return True
    else:
        return False

