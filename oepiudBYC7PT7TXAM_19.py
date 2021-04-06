
def parse_roman_numeral(n):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum([-d[n[i]] if d[n[i]] < d[n[i + 1]] else d[n[i]] for i in range(len(n) - 1)]) + d[n[-1]]

