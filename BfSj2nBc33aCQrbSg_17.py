
def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, num // 2 + 2, 2):
            if num % i == 0:
                return False
        return True
​
def truncatable(n):
    left = True
    right = True
    if not isPrime(n) or "0" in str(n):
        return False
    for i in range(1, len(str(n))):
        if not isPrime(int(str(n)[i:])):
            left = False
        if not isPrime(int(str(n)[0:len(str(n))-i])):
            right = False
    if left and right:
        return "both"
    elif left:
        return "left"
    elif right:
        return "right"
    else:
        return False

