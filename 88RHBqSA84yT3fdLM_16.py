
def inator_inator(inv):
    n = len(inv)
    if inv[-1] in 'AEIOUaeiou':
        inv += '-inator'
    else:
        inv += 'inator'
    return inv + ' '+str(n)+'000'

