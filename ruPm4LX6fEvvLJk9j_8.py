
def esthetic(num):
    ans = []
    for i in range(2,11):
        changed = change_base(i,num)
        if all([abs(x - y) == 1 for x,y in zip(changed,changed[1:])]):
            ans.append(i)
    return 'Anti-Esthetic' if not ans else ans
    
def change_base(i,num):
    c = []
    while num:
        c.append(num % i)
        num //= i 
    return c[::-1]

