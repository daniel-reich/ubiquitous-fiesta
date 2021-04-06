
def secret_word(s,length):
    d=[]
    for i in range(len(s)-2):
        d.append(sum(ord(s[i+k])-96 for k in range(3)))
    for i in range(len(d)):
        for x in range(1,76):
            count=1
            ans=[i+1] 
            for y in range(i+1,len(d)):    
                if d[i]+count*x==d[y]:
                    count+=1
                    ans.append(y+1)
                    if count==length:
                        return ''.join([s[i] for i in ans])

