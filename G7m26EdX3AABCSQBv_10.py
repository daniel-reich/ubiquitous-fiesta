
def format_ascii(txt, width):
  return '\n'.join(txt[x:x+width] for x in range(0,len(txt),width))

