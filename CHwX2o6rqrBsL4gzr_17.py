
def check_title(txt):
  A=txt.split()
  return all(x[0].isupper() for x in A)

