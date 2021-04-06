
def find_it(items, name):
  if name.lower() in items.keys():
    return name.title() + " is gone..."
  else:
    return name.title() + " is here!"

