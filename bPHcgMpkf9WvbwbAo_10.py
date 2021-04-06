
def format_phone_number(lst):
    first, mid, last = '', '', ''
    for num in lst:
        if len(first) <= 2:
            first += str(num)
        elif len(mid) <= 2 and len(first) == 3:
            mid += str(num)
        elif len(mid) <= 3 and len(first) <= 3 and len(last) <= 3:
            last += str(num)
    string = '(%s) %s-%s' % (first, mid, last)
    return string

