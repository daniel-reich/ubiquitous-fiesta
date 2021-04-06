
def final_countdown(lst):
    seq='987654321'
    k=0;ans=[]
    s=''.join([str(i) for i in lst])
    sc=''
    while len(s)>1 and sc!=s:
        sc=s[:]
        fl=0
        for a in range(len(s)):
            for b in range(len(s),a,-1):
                if s[a:b] in seq and s[a:b] not in '23456789' and s[a:b][-1]=='1':
                    fl=1
                    k+=1
                    ans.append([int(i) for i in s[a:b]])
                    s=s[:a]+s[b:]
                    if s=='1':
                        k+=1
                        ans.append([1])
                    break
            if fl==1:break
    return [k,ans]

