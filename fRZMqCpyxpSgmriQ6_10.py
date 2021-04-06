
def sorting(s):
    lower = ''
    upper = ''
    number = ''
    for i in s:
        if i.isdigit():
            number += i
        elif i.islower():
            lower += i
        else:
            upper += i
    sort_nums = ''.join(sorted(number))
    sort_upper = ''.join(sorted(upper))
    sort_lower = ''.join(sorted(lower))
    sort_digits = sort_lower + sort_upper
    sort_digits = ''.join(sorted(sort_digits, key=lambda v: v.upper()))
    return sort_digits + sort_nums

