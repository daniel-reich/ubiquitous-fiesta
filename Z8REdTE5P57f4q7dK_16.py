
def collatz(n):
    list1 = [n]
    if n<1:
        return []
    while n>1:
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1
        list1.append(n)        
    return tuple([len(list1),int(max(list1))])

