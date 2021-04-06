
def lambda_depth(num):
    return eval('lambda num:' + 'lambda :' * num + '"edabit"')(num)

