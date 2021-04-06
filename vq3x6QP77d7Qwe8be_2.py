
def has_odd_patch(lst, size):
    for ii in range(1+len(lst)-size):
        for jj in range(1+len(lst[0])-size):
            square = [row[jj:jj+size] for row in lst[ii:ii+size]]
            if square and all(num%2 for row in square for num in row):
                return True
def odd_square_patch(lst):
    for size in range(min(len(lst), len(lst[0])),0,-1):
        if has_odd_patch(lst, size):
            return size
    return 0

