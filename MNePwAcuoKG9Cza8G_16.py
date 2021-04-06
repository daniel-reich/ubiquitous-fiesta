
def build_staircase(height, block):
    
    lst3=[]
    if height!=0:
        for i in range(1,height+1):
            lst=[]
            for j in range(i):
                lst.append(block)
            for k in range(height-i):    
            
                 lst.append('_')
            print("")
            #print(i,height-i)
            #print(lst)
            lst3.append(lst)
        return(lst3)
        
    else:
       return lst3

