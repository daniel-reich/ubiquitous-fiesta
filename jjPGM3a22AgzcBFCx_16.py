
def decrypt(lst):
  return chr(96 + list(set([x for x in range(1,27)]) - set(lst))[0]).upper()

