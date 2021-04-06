
def doubleton(n):
    digits = []
    n = int(n + 1)
​
    while True:
        for num in str(n):
            if num in digits:
                continue
            else:
                digits.append(num)
        
        if len(digits) != 2:
            digits = []
            n = n+1
        else:
            return n
            break

