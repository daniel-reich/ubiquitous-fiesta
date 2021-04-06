
def expanded_form(num):
    s = str(num)
    return ' + '.join([x[0] + '0' * (len(s[i:]) - 1)
                       for i, x in enumerate(s) if x != '0'])

