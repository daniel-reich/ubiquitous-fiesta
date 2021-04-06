
def even_odd_transform(lst, n):
    for i in range(0, len(lst), 1):
        if lst[i]%2 == 0:
            lst[i]  -= n*2
        else:
            lst[i] += n*2
    return lst

