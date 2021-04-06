
def oddish_or_evenish(num):
    lst = []
    for digito in range(len(str(num))):
        lst.append((int(str(num)[digito])))
    if sum(lst)%2 !=0:
        return 'Oddish'
    else:
        return 'Evenish'

