
def turn_calc(num):
  d = {'1': 'I', '2': 'Z', '3': 'E', '4': 'H', '5': 'S', '6': 'G', '7': 'L', '8': 'B', '.': '', '0':  'O'}
  return str(num)[::-1].translate(str(num).maketrans(d))

