
def find_bob(names):
  i=0
  for name in names:
    try:
      return names.index('Bob')
    except ValueError:
      return -1

