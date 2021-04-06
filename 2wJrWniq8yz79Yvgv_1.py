
def is_narcissistic(n):
    numberLenght = len((str(n)))
    result = 0
    for char in range(0, numberLenght):
        num = str(n)[char]
        result += int(num) ** numberLenght
    if result == n:
        return True
    else:
        return False

