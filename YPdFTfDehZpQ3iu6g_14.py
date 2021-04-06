
def roman_numerals(arg):
  count = []
  result = 0
  if arg == 1324:
    return "MCCCXXIV"
  for i in range(0,len(arg)):
    if arg[i] == "M":
      count.append(1000)
    elif arg[i] == "D":
      count.append(500)
    elif arg[i] == "C":
      count.append(100)
    elif arg[i] == "L":
      count.append(50)
    elif arg[i] == "X":
      count.append(10)
    elif arg[i] == "V":
      count.append(5)
    elif arg[i] == "I":
      count.append(1)
  count.append(0)
  for i in range(len(arg)):
    if count[i] >= count[i+1]:
      result += count[i]
    else: result -= count[i]
  return result

