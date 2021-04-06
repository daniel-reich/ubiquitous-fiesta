
def digit_count(num):
    num = str(num)
    return int(''.join([str(num.count(i)) for i in num]))

