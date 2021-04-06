
def oddish_or_evenish(num):
    if sum(int(n) for n in str(num)) % 2:
        return 'Oddish'
    return 'Evenish'

