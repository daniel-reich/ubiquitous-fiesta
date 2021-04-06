
def almost_sorted(lst):
    for i in range(2):
        x = is_inc(lst)
        if x == -1:
            return False
        # try removing item at index x+1
        y = is_inc(lst[:x+1] + lst[x+2:])
        if y == -1:
            return True
        # try removing item at index x
        z = is_inc(lst[:x] + lst[x+1:])
        if z == -1:
            return True
        # check if desc by using reversed list
        lst = lst[::-1] 
    return False
​
def is_inc(a):
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            return i
    return -1

