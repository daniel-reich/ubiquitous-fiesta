
def prime_in_range(n1, n2):
    for i in range(n1,n2+1):
        p = [i for x in range(2,i//2) if i%x==0]
        if len(p)==0:  return True
    return False

