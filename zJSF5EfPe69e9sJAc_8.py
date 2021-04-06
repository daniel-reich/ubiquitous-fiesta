
def censor_string(txt, lst, char):
  temp = txt.split()
  for i in range(0,len(temp)):
    if temp[i] in lst:
      temp[i]=char*len(temp[i])
  return " ".join(temp)

