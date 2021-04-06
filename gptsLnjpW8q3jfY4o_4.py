
def nCr(n, r):
    x = 1
    y = 1
    for i in range(min(r,n-r)):
        x *= n - i
    for j in range(1,min(r,n-r)+1):
        y *= j
    return int(x/y)
​
def Formula(n):
    if n == 0:
        return "1"
    elif n == 1:
        return "a+b"
    elif n == 2:
        return "a^2+2ab+b^2"
    elif n > 0:
        ans = "a^" + str(n) + "+" + str(n) + "a^" + str(n-1) + "b"
        for i in range(2,n-1):
            ans += "+" + str(nCr(n,i)) + "a^" + str(n-i) + "b^" + str(i)
        ans += "+" + str(n) + "a" + "b^" + str(n-1) + "+b^" + str(n)
        return ans
    else:
        return "1/(" + Formula(-n) + ")"

