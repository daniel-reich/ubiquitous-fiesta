
def expanded_form(num):
    num_str = str(num)
    integer, fractional = num_str.split('.')
    integer_form = ''
    count_dozens = len(integer) - 1
    for num in integer:
        if num != '0':
            integer_form += str(int(num) * (10 ** count_dozens)) + ' + '
        count_dozens -= 1
    count_dozens = 1
    for num in fractional:
        if num != '0':
            integer_form += str(int(num)) + '/' + str(10 ** count_dozens) + ' + '
        count_dozens += 1
    return integer_form[:-3]

