
def camelCasing(txt):
  a = txt.replace('_',' ').split(' ')
  return a[0].lower() + ''.join(i.title() for i in a[1:])

