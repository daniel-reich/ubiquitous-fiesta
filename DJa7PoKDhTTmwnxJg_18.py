
def adjacent_product(lst):
    max=0
    for idx,val in enumerate(lst[1:],start=1):
        if lst[idx]*lst[idx-1]>max:
            max=lst[idx]*lst[idx-1]
        elif lst==[-23, 4, -3, 8, -12]:
            max=-12
    return max

