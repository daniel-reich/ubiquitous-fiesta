
def format_phone_number(lst):
    lst_str = [str(x) for x in lst]
    phoneNumber = '(' + ''.join(lst_str[0:3]) + ')' + ' ' + ''.join(lst_str[3:6]) + '-' + ''.join(lst_str[6:])
    return phoneNumber

