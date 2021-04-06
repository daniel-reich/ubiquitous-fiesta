
def josephus(n, k):
    lst = [i for i in range(0,n)]
    killer = 0
    while len(lst) > 1:
        while killer+k-1 >= len(lst):
            killer = killer-len(lst)
        del lst[killer+k-1]
        killer = killer+k-1
        
    return lst[0]+1

