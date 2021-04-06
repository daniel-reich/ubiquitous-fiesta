
def accumulating_list(list1):
    return [sum(list1[:i+1]) for i in range(len(list1))]

