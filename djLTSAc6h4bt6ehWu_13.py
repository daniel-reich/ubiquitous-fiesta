
def camelCasing(txt):
  lst = txt.lower().replace('_', ' ').split()
  return lst[0] + ''.join([lst[i].title() for i in range(1,len(lst))])

