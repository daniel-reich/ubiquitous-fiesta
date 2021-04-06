
def valid_credit_card(number):
    lst = list(map(int, str(number)))
    a = lst[:]
    a[1::2] = [int(str(x*2)[0]) + int(str(x*2)[1]) if x >= 5 else x*2 for x in a[1::2]]
    lst[::2] = [int(str(x*2)[0]) + int(str(x*2)[1]) if x >= 5 else x*2 for x in lst[::2]]
    
    return not sum(lst) % 10 or not sum(a) % 10

