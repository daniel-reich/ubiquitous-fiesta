
def make_fun_lst(n1, n2):
    
    def get_fn(k):
        if k%2: return lambda x: x * k
        else: return lambda x: x + k
​
    return [get_fn(k) for k in range(n1, n2)]

