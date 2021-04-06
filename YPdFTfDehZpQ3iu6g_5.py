
def roman_numerals(arg):
  templ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  symb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  result = 0
  res_num = ''
  j = 0
​
  if isinstance(arg, str):
      for i in range(len(arg)):
          if i > 0 and templ[arg[i]] > templ[arg[i - 1]]:
              result += templ[arg[i]] - 2 * templ[arg[i - 1]]
          else:
              result += templ[arg[i]]
      return result
  else:
      while arg > 0:
          for p in range(arg // vals[j]):
              res_num += symb[j]
              arg -= vals[j]
          j += 1
      return res_num

