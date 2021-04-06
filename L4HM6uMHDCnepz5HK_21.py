
def halloween(dt):
    ld = [i for i in dt.split('/')]
    for i in range(len(ld)):
        if ld[-1] == '31' and ld[-2] == '10':
            return 'Bonfire toffee'
        else:
            return 'toffee'

