
def parse_roman_numeral(num):
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    v = [d[x] for x in num] + [0]
    return sum([v[i] if v[i] >= v[i+1] else -v[i]
             for i in range(len(num))])

