
def make_fun_lst(n1, n2): 
    return  [create_func(k) for k in range (n1,n2)]
def create_func(k):
    if  k%2 == 0:
        return lambda x : x + k 
    else:
        return lambda x : x * k

