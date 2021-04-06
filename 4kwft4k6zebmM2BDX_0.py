
 def chi_squared_test(data):
    a, b = data['E']
    c, d = data['T']
    chi = round(((a*d - b*c)**2 * (a+b+c+d)) / ((a+b)*(c+d)*(b+d)*(a+c)), 1)
    
    if chi <= 3.841:
        return [chi, 'Edabitin is ininfluent']
    return [chi, 'Edabitin effectiveness = {}%'.format(99 if chi > 6.635 else 95)]

