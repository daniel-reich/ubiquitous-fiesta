
def show_the_love(lst):
    smallest = min(lst)
    adder = 0
    index = lst.index(smallest)
    for idx, x in enumerate(lst):
        if x != smallest:
            lst[idx] = x*0.75
            adder = adder + x*0.25
    
    lst[index] = lst[index] + adder
    
    return lst

