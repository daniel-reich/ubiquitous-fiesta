
def find_bob(names):
  test = "Bob"
  try:
    a = names.index(test)
    return a
  except:
    return -1

