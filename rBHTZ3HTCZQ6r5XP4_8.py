
def expanded_form(num):
    n , d = str(num).split('.')
    temp = []
    temp2 = []
    for idx,num in enumerate(n[::-1]):
        if num != '0':
            temp = [str(int(num) * 10 ** idx)] + temp
    for idx,num in enumerate(d):
        if num != '0':
            temp2 += [num + '/' + str(10 ** (idx + 1))]
    return ' + '.join(temp + temp2)

