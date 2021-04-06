
match = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
numerals = [['', 'M', 'MM', 'MMM'], 
        ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]
def roman_numerals(arg):
    if type(arg) == int:
        roman = ''
        for index,num in enumerate(list(str(arg).zfill(4)), 0):
            roman += (numerals[index][int(num)])
        return roman
    else:
        prev = nums = 0 
        for i in range(len(arg)-1, -1, -1):
            if match[arg[i]] < prev :
                nums -= match[arg[i]]
            else:
                nums += match[arg[i]]
            prev = match[arg[i]]
    return nums
roman_numerals(139)

