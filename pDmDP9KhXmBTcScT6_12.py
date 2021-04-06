
def get_name(address):
  s = address.split("@")
  s.pop()
  newstring = ""
  for x in s[0]:
    if x.isalpha() == True:
      newstring += x
  return newstring

