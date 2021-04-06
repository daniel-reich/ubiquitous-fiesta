
def sig_figs(num):
    n = num.lstrip('-0.')
    return len(n)-('.' in n) if '.' in num else len(n.rstrip('0'))

