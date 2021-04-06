
def get_frequencies(lst):
  lst2=lst
  dic={}
  for ele in lst:
    i=0
    if ele not in dic.keys():
      for ele2 in lst2:
        if ele==ele2:
          i+=1
      dic[ele]=i
  return dic

