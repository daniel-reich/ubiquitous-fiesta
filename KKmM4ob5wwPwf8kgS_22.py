
def get_frequencies(lst):
  dict1={}
  set_list=list(set(lst))
  for i in range(len(set_list)):
    dict1[set_list[i]]=lst.count(set_list[i])
  return dict1

