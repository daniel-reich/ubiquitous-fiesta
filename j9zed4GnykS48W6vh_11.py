
def digits(number):
    a = str(number)
    if a == '1':
        return 0
    index = -1
    for x in range(len(a)):
        if x == 0:
            var_1 = (int(a[index:])) * (abs(index))
            var_2 = 0
            index -= 1
        else:
            var_1 = (int(a[index:]) - 10**(x)) * (abs(index))
            var_2 += int('9' + ('0' * (x - 1))) * (x)             
            index -= 1
    return var_1 + var_2

