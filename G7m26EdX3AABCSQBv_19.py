
def format_ascii(txt, width):
  r = ""
  for i in range(len(txt)):
    r += txt[i]
    if (i+1)%width == 0:
      r += '\n'
  return r[:-1]

