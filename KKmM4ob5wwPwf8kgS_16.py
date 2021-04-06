
def get_frequencies(lst):
  dic={}
  for x in lst:
    if x in dic:
      dic[x]=dic[x]+1
    else:
      dic[x]=1
  return dic

