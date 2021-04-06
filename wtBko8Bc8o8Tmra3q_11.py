
def halflife_calculator(mass, hlife, n):
    mass_left = mass/(2**n)
    years = hlife * n
​
    return [round(mass_left,3),years]

