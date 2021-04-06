
def convert(deg):
    if '*' not in deg:return 'Error'
    val = int(deg.split('*')[0])
    inFahrenheit = round(val * 1.8 + 32)
    inCelsius = round((val - 32) / 1.8)
    return str(inCelsius)+'*C' if 'F' in deg else str(inFahrenheit) + '*F'

