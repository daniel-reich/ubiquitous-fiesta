
def decrypt(t):
    ans=''
    alf='abcdefghiklmnopqrstuvwxyz'
    for i in range(0,len(t)-1,2):
        row=(int(t[i])-1)*5
        col=int(t[i+1])
        ans+=alf[row+col-1]
    return ans
        
def encrypt(t):
    ans=''
    alf='abcdefghiklmnopqrstuvwxyz'
    for i in range(len(t)): 
        for j in range(len(t[i])):
            p=alf.find(t[i][j].lower())
            if t[i][j].lower()=='j':p=8
            if p!=-1:
                row=p//5+1
                col=p%5+1
                ans+=str(row)+str(col)
    return ans        
​
def bifid(text):
    if chr(32) in text:
        t=text.split()    
        t1=encrypt(t)
        t2=[t1[a] for a in range(0,len(t1),2)]
        t3=[t1[a] for a in range(1,len(t1),2)]
        t2.extend(t3)
        t=''.join(t2)
        return decrypt(t)
    else:
        t=text.split()
        t1=encrypt(t)
        d=len(t1)//2
        t2=[t1[a]+t1[a+d] for a in range(d)]
        t=''.join(t2)
        return decrypt(t)

