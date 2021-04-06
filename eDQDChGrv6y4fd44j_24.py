
def can_put(txt, dim):
  lst=txt.split(' ')
  return False if dim[0]==1 and dim[1]<len(txt) or len(lst[-1])>dim[1] else True

