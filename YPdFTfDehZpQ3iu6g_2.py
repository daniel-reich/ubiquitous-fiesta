
roman_numerals=lambda x: (roman if isinstance(x, int) else arabic)(x)
values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
numeral = {v: k for k, v in values.items()}
def roman(n):
  def digit(n, base):
    if n==10: return numeral[10*base]
    s=numerals[5*base] if n>=5 else ""
    if n%5==4: s += numeral[base] + numeral[5*base]
    else: s += numeral[base]*(n%5)
    return s
  return 'M'*(n//1000) + digit(n%1000//100,  100) + digit(n%100//10, 10) + digit(n%10, 1)
def arabic(r):
  vals = [values[c] for c in r] + [0]
  return sum(-x if x<n else x for (x, n) in zip(vals, vals[1:]))

