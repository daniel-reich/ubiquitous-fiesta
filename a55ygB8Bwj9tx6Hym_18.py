
def steps_to_convert(txt):
  uCount = 0
  lCount = 0
  for i in txt:
    if i.islower():
      lCount +=1
    else:
      uCount +=1
  
  if uCount > lCount:
    return lCount
  else:
    return uCount

