
def num_split(num):
    sign = 1 if num >= 0 else -1
    num, res, power = abs(num), [], 0
    while num:
        num, rem = divmod(num, 10)
        res.append(sign * rem * pow(10, power))
        power += 1
    return res[::-1]

