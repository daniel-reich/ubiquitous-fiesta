
def resistor_code(colors):
    d = {'black': {'digit': 0, 'mag': 0}, 
         'brown': {'digit': 1, 'mag': 1, 'tol': '+/-1%', 'tcr': ' 100ppm/k'}, 
         'red': {'digit': 2, 'mag': 2, 'tol': '+/-2%', 'tcr': ' 50ppm/k'}, 
         'orange': {'digit': 3, 'mag': 3, 'tcr': ' 15ppm/k'}, 
         'yellow': {'digit': 4, 'mag': 4, 'tcr': ' 25ppm/k'}, 
         'green': {'digit': 5, 'mag': 5, 'tol': '+/-0.5%'}, 
         'blue': {'digit': 6, 'mag': 6, 'tol': '+/-0.25%', 'tcr': ' 10ppm/k'}, 
         'violet': {'digit': 7, 'mag': 7, 'tol': '+/-0.1%', 'tcr': ' 5ppm/k'}, 
         'gray': {'digit': 8, 'mag': 8, 'tol': '+/-0.05%'}, 
         'white': {'digit': 9, 'mag': 9}, 
         'gold': {'mag': -1, 'tol': '+/-5%'}, 
         'silver': {'mag': -2, 'tol': '+/-10%'}}
​
    coeff = d[colors.pop()]['tcr'] if len(colors) == 6 else ''
    res = int(''.join(str(d[col]['digit']) for col in colors[:-2])) * 10**d[colors[-2]]['mag']
    
    if res >= 10**9:
        res = str(res/10**9) + 'G'
    elif res >= 10**6:
        res = str(res/10**6) + 'M'
    elif res >= 10**3:
        res = str(res/10**3) + 'k'
    else:
        res = str(res)
        
    return '{}Ohm {}'.format(res.replace('.0', ''), d[colors.pop()]['tol']) + coeff

