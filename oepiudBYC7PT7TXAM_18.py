
def parse_roman_numeral(num):
  notation = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }
​
  numerics = list(map(lambda char: notation[char], list(num)))
  number = 0
  i = 0
​
  while (i < len(numerics)):
    if (i == len(numerics) - 1):
      number += numerics[i]
​
    elif (numerics[i] >= numerics[i+1]):
      number += numerics[i]
​
    else:
      number += numerics[i+1] - numerics[i]
      i += 1
​
    i += 1
​
  return number

