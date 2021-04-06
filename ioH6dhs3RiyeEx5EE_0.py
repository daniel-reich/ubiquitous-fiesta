
def mul(i):
    return  lambda x: x*i
def som(i):
    return  lambda x: x+i
​
def make_fun_lst(n1, n2):
    return [[som(i), mul(i)][i % 2] for i in range(n1, n2)]

