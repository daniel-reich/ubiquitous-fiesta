
def format_ascii(txt, width):
  lst=[txt[i:i+width] for i in range(0,len(txt),width)]
  return "\n".join(lst)

