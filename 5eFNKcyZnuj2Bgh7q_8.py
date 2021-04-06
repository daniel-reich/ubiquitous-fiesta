
def is_automorphic(n):
  return str(int(n)**2)[-(len(str(n))):] == str(n)

