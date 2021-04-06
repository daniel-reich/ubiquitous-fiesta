
def format_ascii(txt, width):
  count, lst = 0, []
  while txt != "":
    count += 1
    if not count % width:
      lst += [txt[:width]]
      txt = txt[width:]
  lst, new = [x + "\n" for x in lst[:-1]] + [lst[-1]], ""
  for x in lst:
    new += x
  return new

