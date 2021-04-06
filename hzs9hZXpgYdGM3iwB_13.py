
def alternating_caps(txt):
    upper = True
    result = ''
    for x in txt:
        if x.isalpha():
            if upper == True:
                result += x.upper()
                upper = False
            else:
                result += x.lower()
                upper = True
        else:
            result += x
    return result

