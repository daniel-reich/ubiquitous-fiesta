
def special_reverse_string(txt):
  char_stream = filter(lambda c:not c.isspace(), reversed(txt))
  out = []
  for c in txt:
    out_c = None
    if c.isspace():
      out_c = c
    else:
      out_c = next(char_stream)
      out_c = out_c.upper() if c.isupper() else out_c.lower()
    out.append(out_c)
  return ''.join(out)

