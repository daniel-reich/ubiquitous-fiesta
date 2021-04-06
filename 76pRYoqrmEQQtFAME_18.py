
def is_astonishing(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        a = int(str_num[:i])
        b = int(str_num[i:])
        if a <= b:
            if (a + b) * (b - a + 1) / 2 == num:
                return 'AB-Astonishing'
        else:
            if (a + b) * (a - b + 1) / 2 == num:
                return 'BA-Astonishing'
    return False

