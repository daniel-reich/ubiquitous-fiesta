
def kaprekar(num):
    digits = ''.join(sorted(str(num)+'000'))[-4:]
    return num - 6174 and 1 + kaprekar(int(digits[::-1]) - int(digits))

