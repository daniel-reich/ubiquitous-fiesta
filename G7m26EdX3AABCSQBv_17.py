
def format_ascii(txt, width):
  return"\n".join(txt[i:i+width] for i in range(0,len(txt),width))

