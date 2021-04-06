
def n_differences(lst):
​
    return lst[0] if len(lst)==1 else n_differences( [ lst[i+1]-lst[i] for i in range(len(lst)-1) ] )

