
def int_to_vlq(n):
    s, res, last = bin(n)[2:], [], True
    while s:
        last7 = "{:0>7}".format(s[-7:])
        s = s[:-7]
        if last:
            res = [int("0{}".format(last7), 2)] + res
            last = False
        else:
            res = [int("1{}".format(last7), 2)] + res
    return res
​
​
def vlq_to_int(lst):
    s = "".join(bin(n)[3:] for n in lst[:-1])
    s += "{:0>7}".format(bin(lst[-1])[2:])
    return int(s, 2)

