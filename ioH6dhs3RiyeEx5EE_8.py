
def make_fun_lst(n1, n2):
    res = []
    for n in range(n1, n2):
        if not n % 2:
            res.append(eval('lambda x: x+{}'.format(n)))
        else:
            res.append(eval('lambda x: {}*x'.format(n)))
    return res

