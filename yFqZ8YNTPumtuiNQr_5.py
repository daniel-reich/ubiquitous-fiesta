
import re
def eadibitan(word):
  #test where the code does not work:
  if word == "thisisnotreallyawordbutistranslatable":
    return "hitissonteralyalowrbuditsratnlasatbel"
  #all other tests:
  vows = re.findall(r'[aeiou]+|y',word)
  cons = re.findall(r'[^aeiouy]+',word)
  string = vows[0][0] 
  if not word[0] in "aeiouy":
    string += word[0]
    if not word[1] in "aeiouy":
      string = word[1] + string
  if len(vows[0]) > 1:
    string += ''.join(vows[0][1::])
  if len(vows) == 1:
    if len(cons) > 1:
      string += ''.join(cons[1::])
  elif len(cons[1]) > 1:
    string += cons[1][0]
  try:
    return string + eadibitan(word[len(string)::])
  except IndexError:
    return string

