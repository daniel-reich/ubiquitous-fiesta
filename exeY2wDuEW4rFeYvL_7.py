
def ordered_matrix(a, b):
    lis=[]
    i =1
    sublist=[]   
    while a >0:
        
        count =b
        while count > 0:
            sublist.append(i)
            i +=1
            count -=1
        lis.append(sublist)
        sublist =[]
        a -=1
    return lis

