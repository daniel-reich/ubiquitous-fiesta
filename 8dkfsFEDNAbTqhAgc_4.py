
def division(a, b):
    res = [a // b]
    rem = [a % b, a % b]
    period_start = -1
​
    while period_start < 0 < rem[-1]:
        rem[-1] *= 10
        res.append(rem[-1] // b)
        remainder = rem[-1] % b
        if remainder * 10 in rem:
            period_start = rem.index(remainder * 10)
        else:
            rem.append(remainder)
​
    if period_start > 0:
        str_res = '{}.{}({})'.format(res[0], ''.join(str(i) for i in
                                                     res[1: period_start]),
                                     ''.join(str(i) for i in
                                             res[period_start:]))
    else:
        pre_period = ''.join(str(i) for i in res[1:])
        str_res = '{}.{}'.format(res[0], pre_period if pre_period else '0')
    return str_res

