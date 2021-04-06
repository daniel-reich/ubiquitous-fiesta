
def flip_list(lst):
    a = []
    for i in lst:
        if type(i)==int:
            a.append([i])
        elif type(i)==list:
            a.append(*i)
​
    return a

