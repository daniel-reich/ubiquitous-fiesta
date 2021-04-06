
def sort_array(lst):
    new=[]
    while(len(lst)!=0):
        i=min(lst)
        lst.remove(i)
        new.append(i)
    return new

