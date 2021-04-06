
def inatorInator(inv):
    if inv[-1].lower() in 'aeiou':
        return inv + '-inator' + ' ' + str(len(inv)) + '000'
    else:
        return inv + 'inator' + ' ' + str(len(inv)) + '000'

