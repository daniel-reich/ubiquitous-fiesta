
def mubashir_function(a, b):
    c = lambda x:sum(list(map(lambda x:int(x),list(str(x)))))
    return c(a)*c(b)

