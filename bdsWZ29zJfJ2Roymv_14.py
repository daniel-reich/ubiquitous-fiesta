
def swap_two(txt):
  txt = list(txt)
  try:
    for i in range(0,len(txt),+4):
      txt[i+2],txt[i+3],txt[i],txt[i+1] = txt[i:i+4]
  except ValueError:
    return "".join(txt)
  return "".join(txt)

