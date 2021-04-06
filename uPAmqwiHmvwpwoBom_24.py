
def convert_to_roman(num):
  symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
  values_ = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  roman_n = ""
  n_lengh = 0
  
  while num > 0:
    for x in range(num // values_[n_lengh]):
      roman_n = roman_n + symbols[n_lengh]
      num = num - values_[n_lengh]
    n_lengh = n_lengh + 1
  
  return roman_n

