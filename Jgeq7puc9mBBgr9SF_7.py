
def complete_binary(s):
  if len(s) % 8 == 0:
    return s
  elif len(s) < 8:
    return "0" * (8-len(s)) + s
  else:
    return "0" * (8-(len(s)%8)) + s

