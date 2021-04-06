
def check_perfect(num):
    result = []
    for i in range(1, num):
        if num % i == 0:
            result.append(i)
    return sum(result) == num

