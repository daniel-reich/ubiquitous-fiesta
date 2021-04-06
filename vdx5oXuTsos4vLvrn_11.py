
def kaprekar_numbers(start, end):
    num_len = 0
    kap_str = ''
    left,right = '',''
    output = ''
    for num in range(start, end+1):
        num_len = len(str(num))
        square = str(num**2)
        if len(square) == 1:
            if num == int(square):
                kap_str += str(num) + ' '
        else:
            left = square[-num_len:]
            right = square[:len(square)-num_len]
            check = int(right) + int(left)
            if num == check:
                kap_str += str(num) + ' '
    if kap_str == '':
        return "INVALID RANGE"
    else:
        return kap_str[:-1]

