
def funny_numbers(n, p):
    num = sum([int(i) ** idx for idx,i in enumerate(str(n),p)]) 
    ans = divmod(num,n)
    return ans[0] if not ans[1] else None

