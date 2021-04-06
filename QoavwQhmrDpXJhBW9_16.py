
def flip_list(lst):
    x=[]
    for i in lst:
        if type(i)==int:
            x.append([i])
        else:
            x+=i
    return x

