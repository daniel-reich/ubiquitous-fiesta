
def make_sandwich(i, f):
  return ''.join([" bread " + a + " bread " if a==f else a for a in i]).split()

