
def roman_numerals(arg):
  if type(arg).__name__ == "str":
    ref = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    add = 0
    if "IV" in arg or "IX" in arg:
      add -= 2
    if "XL" in arg or "XC" in arg:
      add -= 20
    if "CD" in arg or "CM" in arg:
      add -= 200
    for key in ref.keys():
      add += arg.count(key) * ref[key]
    return add
  total = arg
  ref = {1000 : "M", 500 : "D", 100 : "C", 50 : "L", 10 : "X", 5 : "V", 1 : "I"}
  string = ""
  keys = list(ref.keys())
  
  for key in sorted(keys, reverse = True):
    current = total // key
    if current == 4:
      if key == 100:
        string += "CD"
      elif key == 10:
        string += "XL"
      else:
        string += "IV"
    elif current == 9:
      if key == 100:
        string += "CM"
      elif key == 10:
        string += "XC"
      else:
        string += "IX"
    else:
      string += (ref[key] * (total // key))
    total -= total // key * key
  return string

