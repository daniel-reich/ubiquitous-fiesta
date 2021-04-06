
def same_vowel_group(lst):
  vowels='aeiou'
  v=list(filter(lambda x:x in vowels,lst[0]))
  v=sorted(list(set(v)))
  newlist=[]
  for i in lst:
    t=list(filter(lambda x:x in vowels,i))
    t=sorted(list(set(t)))
    if t==v:
      newlist.append(i)
  return newlist

