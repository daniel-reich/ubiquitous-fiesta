
def oddish_or_evenish(num):
    if sum([int(i) for i in str(num)]) % 2 == 0:
        return 'Evenish'
    return 'Oddish'

