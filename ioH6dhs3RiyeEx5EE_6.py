
def add(n):
    return lambda x: x+n
​
def multiply(n):
    return lambda x: x*n
​
def make_fun_lst(n1, n2):
    return [[add(i), multiply(i)][i % 2] for i in range(n1,n2)]

