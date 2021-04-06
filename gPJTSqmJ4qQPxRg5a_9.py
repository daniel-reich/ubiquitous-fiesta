
def func(num):
    
    a=(list(str(num)))
    b = len(a)
    
    count = 0
    for i in a:
        count = count + (int(i)-b)
    return count

