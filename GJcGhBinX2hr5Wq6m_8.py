
def move_zeros(lst):
    return [i for i in lst if i!=0 or isinstance(i,bool)]+[i for i in lst if i==0 and not isinstance(i,bool)]

