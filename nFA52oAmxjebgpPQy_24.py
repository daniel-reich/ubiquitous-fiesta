
def char_index(word, char):
  first=0
  last=0
  flag=False
  for i in range(len(word)):
    if word[i]==char:
      first=i
      break
  for i in range(len(word)):
    if word[i]==char:
      flag=True
      last=i
  if flag==False:
    return None
  return[first,last]

