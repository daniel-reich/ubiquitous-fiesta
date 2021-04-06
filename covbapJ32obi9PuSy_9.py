
def diamond_arrays(x):
    res =[[i for j in range(i)] for i in range(1,x+1)]
    return res + res[:x-1][::-1]

