
def hats(lst):
    s=0
    t=lst[0]//sum(1/x for x in lst[1])-1
    while s<lst[0]:
        t+=1  
        s=sum(int(t/x) for x in lst[1])  
        if s==lst[0]:
            return str(int(t))+' minute'+'s'*(t>1)

