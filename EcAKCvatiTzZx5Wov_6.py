
color = {
    'black': [0, 0, '', ''],
    'brown': [1, 1, ' +/-1%', ' 100ppm/k'],
    'red': [2, 2, ' +/-2%', ' 50ppm/k'],
    'orange': [3, 3, ' +/-2%', ' 15ppm/k'],
    'yellow': [4, 4, '', ' 25ppm/k'],
    'green': [5, 5, ' +/-0.5%', ''],
    'blue': [6, 6, ' +/-0.25%', ' 10ppm/k'],
    'violet': [7, 7, ' +/-0.1%', ' 5ppm/k'],
    'gray': [8, 8, ' +/-0.05%', ''],
    'white': [9, 9, '', ''],
    'gold': [0, -1, ' +/-5%', ''],
    'silver': [0, -2, ' +/-10%', '']
}
​
​
def resistor_code(colors):
    digits = ''.join(str(color[c][0]) for c in colors[:-2 if len(colors) < 6
                                                      else -3])
    magnitude = color[colors[-2 if len(colors) < 6 else -3]][1]
    tolerance = color[colors[-1 if len(colors) < 6 else -2]][2]
    tcr = '' if len(colors) < 6 else color[colors[-1]][3]
    resistance = int(digits) * pow(10, magnitude)
    p = ['', 'k', 'M', 'G']
    idx_p = 0
    while resistance > 1000:
        resistance /= 1000
        idx_p += 1
    return '{}{}Ohm{}{}'.format(round(resistance)
                                if float(resistance).is_integer()
                                else resistance, p[idx_p], tolerance, tcr)

