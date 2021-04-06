
def bugger(num):
    l,tot=len(str(num)),0
    while(l>1):
        count=1
        for x in str(num):
            count*=int(x)        
        num=count
        l=len(str(num)) 
        tot+=1
    return tot

