
def nearest_chapter(chapt, page):
  lst = [i for i in chapt if abs(chapt[i]-page)==min([abs(chapt[j]-page) for j in chapt])]
  return lst[0] if len(lst)==1 else [i for i in lst if chapt[i]==max([chapt[j] for j in lst])][0]

