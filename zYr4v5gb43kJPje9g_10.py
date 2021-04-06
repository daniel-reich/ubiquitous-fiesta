
def moving_partition(lst):
    return [[lst[:abs(i)], lst[abs(i):]] for i in range(1,len(lst))]

