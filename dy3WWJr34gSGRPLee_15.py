
def makeBox(n):
    lst = []
    if n==1:
        lst.append("#")
    else:
        lst.append("#"*n)
        for i in range(1,n-1):
            lst.append("#"+" "*(n-2)+"#")
            
        lst.append("#"*n) 
    return lst

