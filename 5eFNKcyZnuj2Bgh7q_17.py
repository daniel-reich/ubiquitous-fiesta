
def is_automorphic(n):
  return True if str(n*n)[-(len(str(n))):] == str(n) else False

