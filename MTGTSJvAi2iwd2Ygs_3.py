
def valid_division(d):
    i = d.index("/")
    num = int(d[:i])
    den = int(d[i+1:])
    if den == 0:
        return "invalid"
    return num % den == 0

