
def concat(*args):
  new_tab = []
  for i in range(len(args)):
    new_tab.extend(args[i])
  return new_tab

