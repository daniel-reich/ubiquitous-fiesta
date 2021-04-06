
def lambda_depth(num):
    if num == 0:
        return 'edabit'
    return lambda:lambda_depth(num - 1)

