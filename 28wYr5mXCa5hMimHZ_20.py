
def valid_name(name):
​
  if len(name.split()) < 2:
    return False
  elif len(name.split()) > 3:
    return False
​
  for word in name.split():
    if '.' in word:
      if word.index('.') != 1:
        return False
​
  if min((word == word.capitalize() for word in name.split())):
    if len(name.split()[-1]) > 2:
      if len(name.split()) == 3 and len(name.split()[0]) == 2 and len(name.split()[1]) > 2:
        return False
      return min((len(word) != 1 for word in name.split()))
  return False

