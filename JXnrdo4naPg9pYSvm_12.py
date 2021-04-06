
def frac_round(frac, n):
    x = eval(frac)
    return ('{} rounded to {} decimal places is '.format(frac, n) +
            eval('"{:.' + str(n) + 'f}".format(x)'))

