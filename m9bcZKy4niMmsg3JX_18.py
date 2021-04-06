
def society_name(friends):
  names = []
  for i in friends:
    names.append(i[0].upper())
  return "".join(sorted(names))

