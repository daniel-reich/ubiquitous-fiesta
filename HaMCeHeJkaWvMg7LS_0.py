
def sun_loungers(beach):
    return sum((len(i)-1)//2 for i in '0{}0'.format(beach).split('1'))

