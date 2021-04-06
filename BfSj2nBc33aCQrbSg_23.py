
def truncatable(n):
    def isprime(num):
        for x in range(2, int(num ** 0.5)+1):
            if num % x == 0:
                return False
        return True
​
    n = str(n)
    if '0' in n:
        return False
    trun_left = [False if len(n[x:]) == 1 and n[x:] == '1' else isprime(int(n[x:])) for x in range(len(n))]
    trun_right = [False if len(n[:len(n)-x]) == 1 and n[:len(n)-x] == '1' else isprime(int(n[:len(n)-x])) for x in range(len(n))]
​
    if all(trun_left) and all(trun_right):
        return 'both'
    elif all(trun_left) and not all(trun_right):
        return 'left'
    elif not all(trun_left) and all(trun_right):
        return 'right'
    return False

