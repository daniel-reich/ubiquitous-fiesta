
def even_odd_string(txt):
  return ''.join([txt[i] for i in range(0,len(txt),2)])+' '+''.join([txt[i] for i in range(1,len(txt),2)])

