
def c_cipher(msg, keyword):
    ans=''
    k=len(keyword)
    order=sorted([i for i in keyword])
    if chr(32) in msg:
        msg=msg.lower()
        msg=msg.replace(' ','')
        msg=msg.replace('.','')
        if len(msg)%k!=0:
            msg+='x'*(k*(len(msg)//k+1)-len(msg))
        arr=[[msg[i] for i in range(s*k,s*k+k,1)] for s in range(0,int(len(msg)/k),1)]       
        for i in order:
            p=keyword.find(i)
            for j in range(len(arr)):
                ans+=arr[j][p]
        return ans
    else:
        q=0
        n=int(len(msg)/len(keyword))
        ans= [ [' ' for x in range( k )] for y in range( n ) ]
        for i in order:
            p=keyword.find(i)
            for j in range(n):
                ans[j][p]=msg[q]
                q+=1
        trans=''.join([j for i in ans for j in i])
        return trans

