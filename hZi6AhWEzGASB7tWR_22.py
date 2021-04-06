
def check(lst):
    if incr(lst):
        return 'increasing'
    if incr(lst[::-1]):
        return 'decreasing'
    return 'neither'
​
def incr(x):
    for i in range(len(x)-1):
        if x[i] >= x[i+1]:
            return False
    return True

