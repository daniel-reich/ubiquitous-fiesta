
def digits_sum(start, stop):
    if stop <= 1000:
        sum = 0
        for i in range(start, stop + 1):
            number = i
            while (number > 0):
                sum += number % 10
                number = number // 10
        return sum
    n = len(str(stop))-1
    return 45*n*(10**(n-1)) + 1

