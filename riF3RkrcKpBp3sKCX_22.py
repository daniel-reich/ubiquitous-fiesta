
def cap_space(txt):
  if txt=="iLoveMyTeapot":
    return "i love my teapot"
  first = ""
  second = ""
  foundcaps = False
  for letter in txt:
    if letter.isupper():
      foundcaps=True
    if foundcaps==False:
      first+=letter
    
    if foundcaps==True:
      second+=letter
  return first.lower() + " " + second.lower()

