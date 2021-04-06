
def parse_roman_numeral(num):
  value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
  total = 0
  for i in range(len(num)):
    if i < len(num) - 1 and value[num[i]] < value[num[i+1]]:
      total -= value[num[i]]
    else:
      total += value[num[i]]
  return total

