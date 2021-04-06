
def roman_numerals(arg):
    roman_numeral_map = (
        ('M',  1000),
        ('CM', 900),
        ('D',  500),
        ('CD', 400),
        ('C',  100),
        ('XC', 90),
        ('L',  50),
        ('XL', 40),
        ('X',  10),
        ('IX', 9),
        ('V',  5),
        ('IV', 4),
        ('I',  1)
        )
    if isinstance(arg, str):
        res = 0
        index = 0
        for roman, arab in roman_numeral_map:
            while arg[index : index + len(roman)] == roman:
                res += arab
                index += len(roman)
​
    elif isinstance(arg, int):
        res = ''
        for roman, arab in roman_numeral_map:
            res += arg // arab * roman
            arg %= arab 
    return res

