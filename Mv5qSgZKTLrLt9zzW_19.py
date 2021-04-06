
def get_drink_ID(flavor, ml):
    
    f = ''.join([i.upper()[:3] for i in flavor.split()])
​
    return '{}{}'.format(f, ml.split('ml')[0])

