
def lemonade(bills):
    bank = []
    for i in bills:
        if i==5:
            bank.append(5)
        elif i==10:
            if 5 in bank:
                bank.append(10)
                bank.remove(5)
            else:
                return False
        else:
            if 5 in bank and 10 in bank:
                bank.append(20)
                bank.remove(5)
                bank.remove(10)
            elif bank.count(5)==3:
                bank.append(20)
                bank = sorted(bank)[3:]
            else:
                return False
    return True

