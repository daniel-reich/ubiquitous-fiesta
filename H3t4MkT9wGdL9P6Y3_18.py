
def oddish_or_evenish(num):
    total = 0
    for i in str(num):
        total += int(i)
    if total % 2 == 0:
        return 'Evenish'
    else:
        return 'Oddish'

