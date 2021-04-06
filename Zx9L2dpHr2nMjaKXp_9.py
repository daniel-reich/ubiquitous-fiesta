
def int_to_vlq(n):
    a,b=[],[]
    p,r=0,n
    while r>127:
        r=r//128
        p +=1
    for i in range(p+1):
        a.append((n%(128**(p-i+1))))
    for i in range(p+1):
        if i ==0 :
            b.append((n%(128**(i+1)))//(128**i))
        else: b.append(128+(n%(128**(i+1)))//(128**i))
        n = n - n%(128**(i+1))
    return(b[::-1])    
​
    
def vlq_to_int(lst):
    av=[]
    for i in range(len(lst)):
        av.append((lst[i]-128)*128**(len(lst)-i-1))
    return(sum(av)+128)

