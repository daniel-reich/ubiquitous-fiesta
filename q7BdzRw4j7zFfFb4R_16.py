
def merge_arrays(a, b):
    a_copy = list(a)
    b_copy = list(b)
    c = list()
    
    if len(a) > len(b):
        long_list = list(a)
    else:
        long_list = list(b)
​
    for i in range(len(long_list)):
        if a_copy:
            c.append(a_copy.pop(0))
        if b_copy:
            c.append(b_copy.pop(0))
    return c

