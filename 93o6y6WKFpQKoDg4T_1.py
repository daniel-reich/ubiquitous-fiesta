
def sort_by_length(lst):
  dic = {}
  for item in lst:
    dic.update({len(item):item})
    
  return [dic[i] for i in sorted(dic.keys())]

