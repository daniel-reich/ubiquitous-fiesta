
def midOc(txt):
  count = 0
  countTwo = -1
  
  for ctr in txt:
    countTwo += 1
    if count == 0 and ctr == txt[1]:
      count += 1
    elif count == 1 and ctr == txt[1]:
      return "@ index " + str(countTwo)
    elif txt.count(txt[1]) < 2:
      return "not found"
def findMid(str):
  lstStr = [a for a in str]
  if len(str) % 2 == 0:
    return lstStr[int((len(str)/2)-1)] + lstStr[int(len(str)/2)]
  else:
    return lstStr[int((len(str)/2)-.5)]
def all_about_strings(txt):
  lstTxt = [m for m in txt]
  Attributes = [len(txt),lstTxt[0],lstTxt[-1],findMid(txt),midOc(txt)]
  return Attributes

