
def prime_factors(num):
    lst = []
​
    while num != 1:
        for i in range(2, num + 1):
            if num % i == 0:
                num //= i
                lst.append(i)
                break
​
    return lst

