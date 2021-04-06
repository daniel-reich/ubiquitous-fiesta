
d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
def letters_combinations(n):
    def bk(n,p,r):
        if n=='':r.append(p);return
        for x in d[n[0]]:bk(n[1:],p+x,r)
    r=[]
    if n:bk(n,'',r)
    return set(r)

