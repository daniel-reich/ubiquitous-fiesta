
def parse_roman_numeral(num):
    vals = [('CM', '+900'), ('M', '+1000'), ('CD', '+400'), ('D', '+500'), 
            ('XC', '+90'), ('C', '+100'), ('XL', '+40'), ('L', '+50'), 
            ('IX', '+9'), ('X', '+10'), ('IV', '+4'), ('V', '+5'), ('I', '+1')]
​
    for n, v in vals:
        num = num.replace(n, v)
    return eval(num)

