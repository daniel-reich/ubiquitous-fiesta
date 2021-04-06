
def lambda_depth(num):
    def inner():
        nonlocal num
        if num == 0:
            return "edabit"
        num -= 1
        return inner
    return inner()

