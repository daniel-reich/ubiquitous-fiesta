
def format_ascii(txt, width):
  return "\n".join(txt[i:width+i] for i in range(0,len(txt),width))

