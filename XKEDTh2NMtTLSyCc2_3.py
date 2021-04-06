
def valid_credit_card(number):
    a = [int(i) for i in str(number)[::-1]]
    for digit in range(1,len(a)):
        if digit % 2 != 0:
            a[digit] = a[digit] * 2
            if a[digit] > 9:
                a[digit] -= 9
    if 9*(sum(a[:-1])) % 10 == a[-1]:
        return True
    return False

