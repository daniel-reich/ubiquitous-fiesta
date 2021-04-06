
def get_diagonals(lst):
    lst1=[]
    lst2=[]
    i=0
    for x in lst:        
        lst1.append(x[i])                                     
        lst2.append(x[len(x)-1-i])
        i+=1
    return([lst1,lst2])

