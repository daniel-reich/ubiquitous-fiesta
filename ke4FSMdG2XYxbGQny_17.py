
def even_odd_transform(lst,n) : 
    v = n * 2 
    l1 = [] 
    for i in lst : 
        if ( i% 2 == 0 ) :  
            l1.append(i-v)
        else : 
            l1.append(i+v) 
    return l1

