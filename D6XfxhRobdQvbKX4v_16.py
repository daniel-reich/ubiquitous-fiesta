
def first_before_second(s, first, second):
    from itertools import product
    first_indices=[i for i,a in enumerate(s) if a==first]
    second_indices=[i for i,a in enumerate(s) if a==second]
    for j in product(first_indices,second_indices):
        if j[0]>j[1]:
            return False
        
    return True

