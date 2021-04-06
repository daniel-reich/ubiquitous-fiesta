
def camelCasing(txt):
  lst = txt.replace('_',' ').split()
  return ''.join(i.lower() if lst.index(i)==0 else i.title() for i in lst)

