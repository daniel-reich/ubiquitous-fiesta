
def translate(ran, num):
    if ran ** 2 < num:
        return "{} is not in the range [0:{}]".format(num, ran ** 2)
    ran = [x for x in range((ran ** 2) + 1)]
    secret = ran[::-1][num]
    d = ran[num :] + ran[: num] 
    ran = ran[: num + 1][::-1] + ran[num + 1 :][::-1]
    count = -1
    for x, y in zip(ran, d):
        count += 1
        if x == secret:
            s1 = "-" + str(count)
        if y == secret:
            s2 = "+" + str(count)
    if abs(int(s1)) == abs(int(s2)) != 0:
        return "{} or {} ---> {}".format(s2, s1, secret)
    elif abs(int(s1)) < abs(int(s2)):
        return "{} ---> {}".format(s1, secret)
    return "{} ---> {}".format(s2, secret)

