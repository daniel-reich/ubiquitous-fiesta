
def find_all_digits(l):
    digits = set(list('0123456789'))
    i = 0
    while len(digits) > 0 and i < len(l):
        digits -= set(str(l[i]))
        if len(digits) == 0:
            return l[i]
        i += 1
    return 'Missing digits!'

