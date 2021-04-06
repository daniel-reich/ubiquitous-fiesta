
def lambda_depth(num):
    if num == 0:
        return "edabit"
    else:
        return lambda: lambda_depth(num-1)

