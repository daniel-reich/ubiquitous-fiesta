
def convert(bin_str):
    '''
    Returns bin_str converted to 2s complement form
    '''
    #print('bin_str on entry', bin_str)
    bin_str = [str(int(d)^1) for d in list(bin_str.zfill(8))]  # 1s complement
    #print('bin_str 1s comp', bin_str)
    carry = '1'  # need to add 1 to make 2's complement
​
    for i in range(7, -1, -1):
        if carry == '0':
            break
        if bin_str[i] == '1':  # adding 1 to 1
            carry, bin_str[i] = '1', '0'
        else:
            carry, bin_str[i] = '0', '1' # adding 1 to 0 - finished.
​
    return ''.join(d for d in bin_str)  # return converted string
        
​
def eight_bit(expression):
    '''
    Return a tuple(v, bin_expr) where v is the decimal result of expression and
    bin_expr is a string expressing the operation in 8-bit 2's complement form.
    Returns an error message if the expression cannot be performed in 8 bits.
    '''
    result = eval(expression)
    num1, op, num2 = expression.split()
    num1, num2 = int(num1), int(num2)
​
    values = [num1, num2, result]
    for i in range(len(values)):
        if not (-128 <= values[i] <= 127):
            return 'Overflow'  # out of range
​
        values[i] = bin(values[i])
        if values[i][0] == '-':
            values[i] = convert(values[i][3:]) # convert to 2s comp -ve
        else:
            values[i] = values[i][2:]   # positive - just remove '0b'.
​
    return (result, ' '.join([values[0], op, values[1], '=', values[2]]))

