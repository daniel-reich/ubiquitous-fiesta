
def parse_roman_numeral(roman_number):
  """ Return roman_number as an arabic number """
  convert = {'M': 1000, 'D': 500,'C': 100,'L': 50, 'X': 10, 'V': 5, 'I': 1}
  n = previous = convert.get(str(roman_number[-1]))
  for x in roman_number[::-1][1:]:
    if convert.get(x) < previous: n -= convert.get(x)
    else: n += convert.get(x)
    previous = convert.get(x)
  return n

