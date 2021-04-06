
def longest_nonrepeating_substring(txt):
  long,s,start = txt[0],txt[0],0
  for i in range(1, len(txt)):
    if txt[i] not in s:
      s+=txt[i]
      if len(s)>len(long):
        long=s
    else:
      start=txt.index(txt[i])+1
      txt = txt.replace(txt[i], '#', 1)
      s = txt[start:i+1]
  return long

