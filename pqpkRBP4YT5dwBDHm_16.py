
def show_the_love(lst):
    indx = lst.index(min(lst))
    value = lst[lst.index(min(lst))];sm=0
    for i,a in enumerate(lst):
        if i==indx:
            continue
        else:
            lst[i]=lst[i]-a/4
            sm+=a/4
    lst[indx] = value + sm
    return lst

