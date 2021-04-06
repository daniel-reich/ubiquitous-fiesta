
def format_ascii(txt, width):
  x = [[txt[i], txt[i]+'\n'][int((i+1)%width==0 and (i+1)<len(txt))] for i in range(len(txt))]
  return "".join(x)

