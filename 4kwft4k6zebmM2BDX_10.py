
def chi_squared_test(results):
    '''
    Returns the effectiveness of the Edabit influence based on the chi-squared
    test as per the instructions.
    '''
    ALPHA1 = 6.635
    ALPHA5 = 3.841  # 99% & 95% chi-square confidence intervals for this table
​
    table = [[0,0,0] for i in range(3)]  # to hold results & totals etc
    table[2][2] = sum(v[0] + v[1] for _, v in results.items()) # total progs
    table[0][0], table[0][1] = [v for v in results['E']]
    table[1][0], table[1][1] = [v for v in results['T']]  # results in table
    table[0][2], table[1][2] = sum(table[0]), sum(table[1]) # row totals
    table[2][0], table[2][1] = table[0][0] + table[1][0], \
                               table[0][1] + table[1][1]  # col totals
    expected = [[table[i][2]*table[2][j]/table[2][2] for j in range(2)] \
                 for i in range(2)]
    chi_square = round(sum((table[i][j] - expected[i][j])**2/expected[i][j] \
                     for j in range(2) for i in range(2)), 1)
    
    effectiveness = 'Edabitin effectiveness = 99%' if chi_square > ALPHA1 \
                 else 'Edabitin effectiveness = 95%' if chi_square > ALPHA5 \
                 else 'Edabitin is ininfluent'
    
    return [chi_square, effectiveness]

