
def division(n, d):
    units, n = divmod(n, d) 
    rem_dict = { n: 0}
    decimals = []
    while n > 0:
        dec, n = divmod(n * 10, d)
        decimals.append(dec)
        if n in rem_dict:
            return str(units) + '.' + ''.join(map(str, decimals[:rem_dict[n]])) + '(' + ''.join(map(str, decimals[rem_dict[n]:])) + ')'
        else:
            rem_dict[n] = len(decimals)
    return str(units) + '.' + (''.join(map(str, decimals)) if len(decimals) > 0 else '0')

