
def calc(s):
    num1 = ''
    num2 = ''
    sum1 = 0
    sum2 = 0
    for n in s:
        num1 += str(ord(n))
    for i in num1:
        if int(i) == 7:
            num2 += str(1)
        else:
            num2 += str(i)
    for l in num1:
        sum1 += int(l)
    for l in num2:
        sum2 += int(l)
    return sum1-sum2

