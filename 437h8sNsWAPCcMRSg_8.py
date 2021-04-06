
def product_of_primes(num):
    arrFactor = []
    arrMulti = []
    multiplier = 2
    while num != 1:
        if divmod(num,multiplier)[1] == 0:
            if multiplier in arrFactor:
                arrMulti[len(arrMulti)-1] += 1
            else:
                arrFactor.append(multiplier)
                arrMulti.append(1)
            num = num / multiplier
        else:
            multiplier += 1
​
​
​
    if len(arrFactor) == 1 and arrMulti[0] == 2:
        return True
    elif len(arrFactor) == 2:
        if arrMulti[0] == 1 and arrMulti[1] == 1:
            return True
        else:
            return False
    else:
        return False

