
def is_factorial(n):
    index = 0
    result = 1
    while True:
        index += 1
        result += result * index
        if result > n:
            return False
        elif result == n:
            return True

