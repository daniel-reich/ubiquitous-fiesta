
def next_prime(num):
    if num<2:
        return 2
    def is_prime(num):
        if num in range(2,4):
            return True
        res=[num%x for x in range(2,(num//2)+1)]
        if 0 in res:
            return False
        else:
            return True
​
    if is_prime(num):
        return(num)
    return next_prime(num+1)

