
------------------------------------------
​
def prime(n):
    if len([i for i in range(1,n+1) if n%i ==0]) <=2:return True
    else:return False
​
def is_unprimeable(num):
    l = []
    if prime(num) : return "Prime Input"
    if num == 1: return [2,3,5,7]
    t = 0
    num = str(num)
    for i in (str(num)):
        n = []
        for j in range(1,10):
            n = [str(num[x]) for x in range(len(str(num))) if x !=t ]
            n.insert(t, str(j))
            if prime(int("".join(n))):
                l.append(int("".join(n)))
        t+=1
    if len(l)>=1:return l
    else: return "Unprimeable"

