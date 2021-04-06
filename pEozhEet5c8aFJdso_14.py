
def all_about_strings(txt):
  res = [0]*5
  res[0] = len(txt)
  res[1] = txt[0]
  res[2] = txt[-1]
  mid = len(txt)//2
  if len(txt)%2==1:
    res[3] = txt[mid]
  else:
    res[3] = txt[mid-1:mid+1]
  pos = -1
  for i in range(2,len(txt)):
    if txt[i]==txt[1]:
      pos=i
      break
  if pos != -1:
    res[4]  = "@ index " + str(pos)
  else:
    res[4] = "not found"
  return res

