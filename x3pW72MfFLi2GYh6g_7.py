
def is_scalable(lst):
    return all(lst[i]-lst[i-1]<=5 for i in range(1,len(lst)))

