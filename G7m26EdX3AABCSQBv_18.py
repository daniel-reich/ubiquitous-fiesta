
def format_ascii(txt, width):
  return "\n".join(txt[n:n+width] for n in range(0,len(txt),width))

