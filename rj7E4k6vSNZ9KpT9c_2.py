
def factor_chain(lst):
    return not bool([i for i in lst if lst[-1] % i != 0])

