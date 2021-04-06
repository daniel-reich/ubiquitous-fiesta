
def parse_roman_numeral(num):
  d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
  count = 0
  last = 1000
  for i in [d[i] for i in num]:
    c = i
    count += i
    if last < i:
      count -= last*2
    last = i
  return count

