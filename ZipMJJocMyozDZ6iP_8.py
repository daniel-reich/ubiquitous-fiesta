
def group(lst, size):
    result = [[] for i in range(len(lst)//size + (len(lst) % size > 0))]    
    for elem in lst:
        result[lst.index(elem) % len(result)].append(elem)
    return result

