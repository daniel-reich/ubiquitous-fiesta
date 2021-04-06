
def valid_credit_card(number):
    sayi = list(str(number)[::-1])
    for i in range(1, len(sayi),2):
        sayi[i] = int(sayi[i])*2
        if sayi[i] > 9: sayi[i] -= 9
    total = 0
    for i in sayi[1:]: total += int(i)
    return (total * 9)%10 == int(sayi[0])

