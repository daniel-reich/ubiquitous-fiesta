
def turn_calc(num):
  num = str(num)[::-1]
  letters = {'1':'I','2':'Z','3': 'E','4': 'H','5': 'S','6': 'G','7': 'L','8': 'B','9': '-','0': 'O'}
  emptystring = ''
  for eachdigit in num:
    if eachdigit in letters.keys():
      emptystring += letters[eachdigit]
  return emptystring

