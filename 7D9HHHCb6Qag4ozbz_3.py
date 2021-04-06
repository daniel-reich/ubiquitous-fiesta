
def find_zip(t):
  p=t.rfind('zip')
  return(-1,p)[p!=t.find('zip')]

