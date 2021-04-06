
def convert_to_roman(num):
  base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  numeral = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
  final = ''
  for i in range(13):
    while num >= base[i]:
      final += numeral[i]
      num -= base[i]
  return final

