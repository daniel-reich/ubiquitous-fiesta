
def palindrome_type(num):
    decimal_flag = str(num) == str(num)[::-1]
    binary_flag = str(bin(num))[2:] == str(bin(num))[2:][::-1]
​
    if decimal_flag and binary_flag:
        return "Decimal and binary."
    else:
        if decimal_flag:
            return "Decimal only."
        elif binary_flag:
            return "Binary only."
        else:
            return "Neither!"

