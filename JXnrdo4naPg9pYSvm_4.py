
def frac_round(frac, n):
    value=round(eval(frac), n)
    value_str=str(value)
    ind = value_str[value_str.index(".")+1:]
    if len(ind) <n:
        value_str += "0" *(n-len(ind))
    else:
        pass
    
    return "{} rounded to {} decimal places is {}" .format(frac, n, value_str)

