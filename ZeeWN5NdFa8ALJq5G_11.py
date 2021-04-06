
def nearest_chapter(chapt, page):
  temp = {}
  for i in chapt.keys():
    temp[i] = abs(chapt[i]-page)
  near = [i for i in temp.keys() if temp[i] == min(temp.values())]
  return sorted(near,key=lambda x: chapt[x])[-1]

