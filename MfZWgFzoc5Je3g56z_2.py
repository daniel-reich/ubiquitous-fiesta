
def translate(ran, num):
    if num < 0 or num > ran**2:
        return str(num) + ' is not in the range [0:' + str(ran**2) + ']'
    secret = ran**2 - num
    steps1 = abs(num - secret)
    steps2 = ran**2 - max(secret, num) + min(secret, num) + 1
    if steps1 < steps2:
        if num > secret:
            ans = '-' + str(steps1)
        else:
            ans = '+' + str(steps1)
    elif steps2 < steps1:
        if num > secret:
            ans = '+' + str(steps2)
        else:
            ans = '-' + str(steps2)
    else:
        ans = '+' + str(steps1) + ' or -' + str(steps2)
    ans += ' ---> ' + str(secret)
    return ans

