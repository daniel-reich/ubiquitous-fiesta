
def mixed_number(frac):
    frac = [int(i) for i in list(frac.split('/'))]
​
    if frac[0] < 0:
        return '-{}'.format(mixed_number('{}/{}'.format(frac[0]*-1, frac[1])))
​
    whole_number = frac[0] // frac[1]
    remainder = frac[0] % frac[1]
    denominator = frac[1]
​
    if remainder == 0:
        return '{}'.format(whole_number)
    for i in range(min(frac[0], frac[1]), 1, -1):
        if remainder % i == 0 and denominator % i == 0:
            denominator //= i
            remainder //= i
            break
    if whole_number == 0:
        return str(remainder) + '/' + str(denominator)
    else:
        return str(whole_number) + ' ' + str(remainder) + '/' + str(denominator)

