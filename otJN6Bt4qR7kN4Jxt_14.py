
def incremental_depth(lst):
    sol = [lst[-1]]
    for i in lst[-2::-1]:
        sol = [i,sol[::]] 
    return sol

