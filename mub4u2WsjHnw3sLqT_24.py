
def lambda_depth(num):
    def loop():
        nonlocal num
        if num == 0:
            return "edabit"
        else:
            num = num - 1
            return loop
    return loop()

