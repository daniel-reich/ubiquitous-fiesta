
def sorting(s):
    import string
    lst = ''
    order = zip(string.ascii_lowercase, string.ascii_uppercase)
    for (l,u) in list(order):
        if l in s:
            lst += l
        if u in s:
            lst += u
    for digit in string.digits:
        if digit in s:
            lst += digit
    return lst

