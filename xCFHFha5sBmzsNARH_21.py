
def reverse(txt):
  if len(txt) in [0,1]:
    return txt
  else:
    return txt[-1]+reverse(txt[:-1])

