
def swap_xy(txt):
  swapped = ''
  txt = txt.replace(',', '')
  txt = txt.replace('(', '')
  txt = txt.replace(')', '')
  txt = txt.split()
  for i in range(0,len(txt),2):
    swapped += '('
    swapped += str(txt[i+1])
    swapped += ', '
    swapped += str(txt[i])
    swapped += '), '
  
  return swapped[:-2]

