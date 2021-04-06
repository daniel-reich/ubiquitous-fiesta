
def get_factors(txt):
    return [i for i in range(1, int(txt)+1) if int(txt) % i == 0 and i != 1]
def simplify(txt):
    f1 = get_factors(txt[0])
    f2 = get_factors(txt[1])
    total = 1
    for i in f1:
        if i in f2:
            if i > total:
                total = i
    num1 = int(int(txt[0]) / total)
    num2 = int(int(txt[1]) / total)
    return (num1, num2)
def mixed_number(txt):
    txt = txt.split('/')
    if (int(txt[0]) / int(txt[1])) % 1 == 0:
        return str(int(int(txt[0]) / int(txt[1])))
    else:
        neg = False
        for i in range(len(txt)):
            if '-' in str(txt[i]):
                txt[i] = txt[i][1:]
                neg = True
        nums = simplify(txt)
        num1,num2 = nums[0],nums[1]
        if num1 > num2:
            print('hi')
            whole = int(num1) // int(num2)
            mod = int(num1) % int(num2)
            if neg:
                return '-' + str(whole) + ' ' + str(mod) + '/' + str(num2)
            else:
                return str(whole) + ' ' + str(mod) + '/' + str(num2)
        else:
            if not neg:
                return str(num1) + '/' + str(num2)
            else:
                return '-' + str(num1) + '/' + str(num2)

