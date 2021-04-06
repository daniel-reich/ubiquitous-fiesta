
def showdown(p1, p2):
    if p1.find('Bang') < p2.find('Bang'):
        return 'p1'
    elif p1.find('Bang') > p2.find('Bang'):
        return 'p2'
    else:
        return 'tie'

