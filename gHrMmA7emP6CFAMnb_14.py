
def is_apocalyptic(number):
    if str(2**number).count('666') == 1:
        return 'Single'
    elif str(2**number).count('666') == 2:
        return 'Double'
    elif str(2**number).count('666') == 3:
        return 'Triple'
    else:
        return 'Safe'

