
def convert_to_roman(num):
  roman = ""
​
  roman += "M" * int(num / 1000)
  num %= 1000
  roman += "CM" * int(num / 900)
  num %= 900
  roman += "D" * int(num / 500)
  num %= 500
  roman += "CD" * int(num / 400)
  num %= 400
  roman += "C" * int(num / 100)
  num %= 100
  roman += "XC" * int(num / 90)
  num %= 90
  roman += "L" * int(num / 50)
  num %= 50
  roman += "XL" * int(num / 40)
  num %= 40
  roman += "X" * int(num / 10)
  num %= 10
  roman += "IX" * int(num / 9)
  num %= 9
  roman += "V" * int(num / 5)
  num %= 5
  roman += "IV" * int(num / 4)
  num %= 4
  roman += "I" * int(num)
  
  return roman

