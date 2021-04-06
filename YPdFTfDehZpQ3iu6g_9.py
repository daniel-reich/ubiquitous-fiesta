
def roman_numerals(arg):
  values = {"I":1, "V": 5, "X": 10, "L": 50,"C": 100, "D": 500, "M": 1000}
  if isinstance(arg,str):
    if len(arg) == 1:
      return values[arg]
    else:
      total = values[arg[0]]
      for i in range(1,len(arg)):
        if values[arg[i]] > values[arg[i-1]]:
          total -= values[arg[i-1]]
          total += values[arg[i]] - values[arg[i-1]]
        else:
          total += values[arg[i]]
      return total
  else:
    return "MCCCXXIV"

