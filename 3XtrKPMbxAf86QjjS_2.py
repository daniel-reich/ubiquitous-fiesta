
def same_case(txt):
  return all(i.isupper() for i in txt) or all(i.islower() for i in txt)

