
def swap_two(x):
  bal = ''
  rem = len(x) % 4
  if rem:
    bal = x[-rem:]
    x = x[:-rem]
  fin = []
  for a,b in zip(range(0,len(x),4), range(2,len(x),4)):
    fin.append(x[b:b+2])
    fin.append(x[a:a+2])
  finword = ''.join(fin)+bal
  return finword

