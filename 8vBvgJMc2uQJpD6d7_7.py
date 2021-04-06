
def prime_factors(num):
    list = []
    n = num
    d = 2
    if n == 0 or n == 1:
        return 0
​
    elif n >= 2:
        while n >= d:
            if n % d == 0:
                list.append(d)
                n = n/d
            else:
                d+=1
        return list

