
def super_digit(n, k):
    sum = 0
    for index in range(0, len(n)):
        sum+=int(n[index])
    
    if sum*k < 10:
        return sum*k
    else:
        return super_digit(str(sum*k), 1)

