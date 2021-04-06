
def prime_gaps(g, a, b):
    ans = []
    for i in range(a,b+1):
        if is_prime(i):
            ans.append(i)
            if len(ans) == 2:
                if ans[1] - ans[0] == g:
                    return ans 
                else:
                    ans.pop(0)
    return None
​
def is_prime(num):
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

