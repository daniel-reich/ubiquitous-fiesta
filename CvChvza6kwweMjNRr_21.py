
def split_code(item):
  s = list(item)
  letters = []
  digits = []
  for i in s:
    if i.isdigit():
      digits.append(i)
    else:
      letters.append(i)
      
  return [''.join(letters), int(''.join(digits))]

