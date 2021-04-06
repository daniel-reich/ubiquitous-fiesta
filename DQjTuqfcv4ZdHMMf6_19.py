
def kaprekar(num, cycle=0):
    if num == 6174:
        return cycle
    return kaprekar(generate_num(num), cycle + 1)
​
def generate_num(num):
    str_num = str(num)
    if num < 1000:
        str_num = '0' + str_num
    return int(''.join(sorted(str_num, reverse=True))) - int(''.join(sorted(str_num)))

