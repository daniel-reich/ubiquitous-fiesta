
from numpy import prod
​
​
def digital_division(n):
    lista = []
    lista.append(divisible_by_each(n))
    lista.append(divisible_by_sum(n))
    lista.append(divisible_by_product(n))
​
    if sum(lista) == 3:
        return 'Perfect'
    elif sum(lista) == 0:
        return 'Indivisible'
    else:
        return sum(lista)
​
​
def divisible_by_each(num):
    temp = list(str(num))
    list_ = []
    for i in temp:
        if int(i) == 0:
            list_.append(True)
            continue
        if num % int(i) == 0:
            list_.append(True)
        else:
            list_.append(False)
    return all(list_)
​
​
def divisible_by_sum(num):
    sum_digits = sum([int(i) for i in str(num)])
    if num % sum_digits == 0:
        return True
    else:
        return False
​
​
def divisible_by_product(num):
    product = prod([int(i) for i in str(num)])
    if product > 0:
        if num % product == 0:
            return True
        else:
            return False
    return False

