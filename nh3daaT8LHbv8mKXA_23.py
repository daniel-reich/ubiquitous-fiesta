
def text_to_num(phone):
  numbers = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}
  x = list(phone)
  for i in range(len(x)):
    for eachkey in numbers.keys():
      if x[i] in eachkey:
        x[i] = str(numbers[eachkey])
  return ''.join(x)

