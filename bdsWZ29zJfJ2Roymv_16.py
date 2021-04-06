
def swap_two(txt):
  if len(txt) < 4:
    return txt
  elif len(txt) % 2 != 0:
    lastletter = txt[-1]
    formattedtxt = txt[:-1]
    emptystring = ''
    for i in range(0,len(txt)-3,4):
      emptystring += txt[i+2:i+4]
      emptystring += txt[i:i+2]
    return emptystring + txt[i+4:]
  else:
    emptystring = ''
    for i in range(0,len(txt)-3,4):
      emptystring += txt[i+2:i+4]
      emptystring += txt[i:i+2]
    return emptystring

