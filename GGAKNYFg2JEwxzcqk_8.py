
def anti_divisors(n):
    new = []
    for i in range(2,n-1):
        if n % i != 0:
            if i % 2 != 0:
                if ((n*2)-1) % i == 0 or ((n*2)+1) % i == 0:
                    new.append(i)
            if i % 2 == 0:
                if (n*2) % i == 0:
                    new.append(i)
    return new

