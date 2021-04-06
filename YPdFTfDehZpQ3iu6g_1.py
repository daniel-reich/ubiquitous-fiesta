
d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
​
def roman_numerals(arg): 
    if isinstance(arg, int):
        res, n = '', int(arg)
        for value, numeral in d:
            res += numeral * (n//value)
            n %= value       
    else:
        res = 0
        while arg:
            for value, numeral in sorted(d, key=lambda x: -len(x[1])):
                if numeral in arg:
                    res += value
                    arg = arg.replace(numeral, '', 1)
    return res

