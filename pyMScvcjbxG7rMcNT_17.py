
def sum_list(lst):
    a=0
    lst=(str(lst))
    for i in lst :
        if i.isdigit():
            a+=int(i)
    return(a)

