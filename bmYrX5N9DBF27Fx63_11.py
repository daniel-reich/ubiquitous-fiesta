
def greatest_impact(factors):
    '''
    Returns the factor (weather, meals, sleep) which has greatest impact on
    mood, given the instructions, or nothing if no single factor predominates.
    '''
    FACTORS = (('Mood',10),('Weather',10),
               ('Meals',3),('Sleep',10))  # Factors and their scales
​
    size = len(factors)
    avgs = [sum(fac)/size/FACTORS[i][1]*100 for i, fac in enumerate(zip(*factors))] 
    if all(avgs[i] == avgs[0] for i in range(1,4)):
        return 'Nothing'
    
    diffs = [abs(avgs[i] - avgs[0]) for i in range(1,4)]
    
    return FACTORS[diffs.index(min(diffs)) + 1][0]

