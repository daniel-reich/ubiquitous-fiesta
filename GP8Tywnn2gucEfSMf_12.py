
def error(n):
    EC={1:"Check the fan", 2:"Emergency stop", 3:"Pump Error", 4:"c",5:"Temperature Sensor Error"}
    return 101 if n not in EC else '{}: e{}'.format(EC[n],n)

