
def convert_to_roman(num):
  #Convert num to 4-digit string
  num = '0'*(4 - len(str(num))) + str(num)
​
  #Roman numeral database
  d = [['', 'M', 'MM', 'MMM'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
  ]
​
  return ''.join([d[x][int(num[x])] for x in [0,1,2,3]])

