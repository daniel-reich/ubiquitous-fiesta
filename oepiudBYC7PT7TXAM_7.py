
values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
​
def parse_roman_numeral(num):
  largest = 0
  total = 0
  for dig in reversed(num):
    val = values[dig]
    total += val if val >= largest else -val
    largest = max(largest, val)
  return total

