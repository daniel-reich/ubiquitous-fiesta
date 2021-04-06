
def find_zip(txt):
  if txt.count("zip") ==1:
    return -1
  for i in range(len(txt)-1,0, -1):
    if txt[i] =='p' and txt[i-1] =='i' and txt[i-2] =='z':
      return i-2

