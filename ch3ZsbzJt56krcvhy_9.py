
def square_root(n):
    r=i=0
    digits=(len(str(n))+(len(str(n))%2==1))//2
    while r!=n:
        i*=10
        r=0
        while r<n:
            i+=1
            s=int(str(i)+'0'*(digits-len(str(i))))
            r=s*s
            if i%10==0:break
        i-=1
    return s

