
def camel_to_snake(s):
  newlist = []
  for eachletter in s:
    if eachletter == eachletter.upper() and eachletter != ' ' and not eachletter.isdigit():
      newlist.append("_")
      newlist.append(eachletter.lower())
    else:
      newlist.append(eachletter)
  return ''.join(newlist)

