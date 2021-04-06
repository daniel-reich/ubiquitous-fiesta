
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
arabic = [1000, 900, 500, 400, 100, 90, 50,40, 10, 9, 5, 4, 1]
def convert_to_roman(num):
  roman_number = ""
  while num > 0:
    x = 0
    while True:
      if num - arabic[x] >= 0:
        num = num- arabic[x]
        roman_number += roman[x]
        break
      x += 1
  return roman_number

