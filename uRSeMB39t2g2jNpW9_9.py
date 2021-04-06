
def turn_calc(num):
  
  converter = {'.': '', '1':  'I', '2': 'Z', '3': 'E', '4': 'H', '5': 'S', '6': 'G', '7': 'L', '8': 'B', '9': '-', '0': 'O'}
  
  return ''.join(list(reversed([converter[n] for n in list(str(num)) if n in converter.keys()])))

