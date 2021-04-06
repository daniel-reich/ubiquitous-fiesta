
def is_legitimate(pool):
    if 1 in pool[0] or 1 in pool[-1]:
        return False
​
    for i in pool:
        if i[0] == 1 or i[-1] == 1:
            return False
​
    return True

