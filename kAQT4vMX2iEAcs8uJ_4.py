
def longest_7segment_word(lst):
  ans=[]
  bad=['k','m','v','w','x']
  for i in lst:
    if not any(item in i for item in bad):
      ans.append(i)
  if ans: return max(ans,key=len)
  return ''

