
def is_unprimeable(num):
    lst = []
    if is_prime(num):
        return 'Prime Input'
    num = str(num)
    for i in range(len(num)):
        for j in range(0, 10):
            if is_prime(int(num[:i]+str(j)+num[i+1:])):
                lst.append(int(num[:i]+str(j)+num[i+1:]))
    return 'Unprimeable' if len(lst) < 1 else sorted(lst)
        
​
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

