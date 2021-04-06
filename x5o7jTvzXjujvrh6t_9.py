
def i_sqrt(n):
    if n < 0:
        return "invalid"
    else:
        sum = 0
        while n >= 2:
            n = n ** (1/2)
            sum += 1
        return sum

