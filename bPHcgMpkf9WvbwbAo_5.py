
def format_phone_number(lst):
    lst = ''.join(str(l) for l in lst)
    return '({}) {}-{}'.format(lst[:3], lst[3:6], lst[6:])

