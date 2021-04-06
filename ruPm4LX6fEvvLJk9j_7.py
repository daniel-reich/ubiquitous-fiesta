
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
def esthetic(num):
    ans=[]
    for b in range(2,11):
        k=0
        a=numberToBase(num,b)
        for c in range(len(a)-1):
            if abs(a[c]-a[c+1])!=1:
                break
            k+=1
        if k==len(a)-1:
            ans.append(b)
    if ans==[]:return'Anti-Esthetic'
    return ans

