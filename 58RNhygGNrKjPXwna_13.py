
def longest_nonrepeating_substring(txt):
  maxi = ""
  for i in range(len(txt)):
    c = txt[i]
    for k in range(i+1,len(txt)):
      if txt[k] not in c:
        c+=txt[k]
      else:
        break
    if len(c) > len(maxi):
      maxi = c
  return maxi

