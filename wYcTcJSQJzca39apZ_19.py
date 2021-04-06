
def truncate(txt, length):
  if len(txt) <= length: return txt
  enum = list(enumerate(txt))
  spaces = [pos for pos, char in enum if char == ' ']
  return txt[:max([0]+[pos for pos in spaces if pos <= length])]

