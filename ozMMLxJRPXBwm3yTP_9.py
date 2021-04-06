
def is_factorial(number, check=1, count=1):
    if number == check:
        return True
    elif number < check:
        return False
    else:
        return is_factorial(number, (count + 1) * check, count + 1)

