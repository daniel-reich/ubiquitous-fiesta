
def get_vowel_substrings(txt):
  lst = []
  v = 'aeiou'
  for i in range(0,len(txt)):
    for x in range(i+1,len(txt)+1):
      if txt[i:x][0].lower() in v and txt[i:x][-1].lower() in v and txt[i:x] not in lst:
        lst.append(txt[i:x])
  return sorted(lst)
​
def get_consonant_substrings(txt):
  lst = []
  c = 'bcdfghjklmnpqrstvwxyz'
  for i in range(0,len(txt)):
    for x in range(i+1,len(txt)+1):
      if txt[i:x][0].lower() in c and txt[i:x][-1].lower() in c and txt[i:x] not in lst:
        lst.append(txt[i:x])
  return sorted(lst)

