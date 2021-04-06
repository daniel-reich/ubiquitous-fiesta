
def find_it(items, name):
  if name in items.keys():
    found = "%s is gone..." % name.capitalize()
  else:
    found = "%s is here!" % name.capitalize()
  return found

