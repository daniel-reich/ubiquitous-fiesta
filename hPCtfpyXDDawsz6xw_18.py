
def verbify(txt):
  lst = txt.split()
  if lst[0].endswith("e"):
    verb = lst[0] + "d"
  elif lst[0].endswith("ed"):
    verb = lst[0]
  else:
    verb = lst[0] + "ed"
  return ''.join(verb + " " + lst[1])

