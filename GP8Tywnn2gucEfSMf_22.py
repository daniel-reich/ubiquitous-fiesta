
def error(n):
    if n in [1,2,3,4,5]:
        x = {
            1: 'Check the fan',
            2: 'Emergency stop',
            3: 'Pump Error',
            4: 'c',
            5: 'Temperature Sensor Error',
            }
        return '{}: e{}'.format(x.get(n), n)
    else:
        return 101

