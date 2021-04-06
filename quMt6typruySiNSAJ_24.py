
def shuffle_count(num):
    n,i=2,1
    while n% (num-1) >1:
        n*=2
        i+=1
    return i

