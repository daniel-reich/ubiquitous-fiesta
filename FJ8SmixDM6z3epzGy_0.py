
def check_perfect(num):
    return sum([i for i in range(1, num) if num%i==0]) == num

