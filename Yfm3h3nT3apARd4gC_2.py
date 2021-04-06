
def rolls(lst):
    return sum(lst[i]*2 if lst[i-1]==6 else 0 if lst[i-1]==1 else lst[i] for i in range(1,len(lst))) + lst[0]

