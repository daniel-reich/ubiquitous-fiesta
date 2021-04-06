
def lemonade(bills):
    num1, num2 = 0, 0
    for i in bills:
        if i == 5:
            num1 += 1
        elif i == 10:
            num1 -= 1
            num2 += 1
        else:
            if num2 > 0:
                num2 -= 1
                num1 -= 1
            else:
                num1 -= 3
    return True if num1 >= 0 else False

