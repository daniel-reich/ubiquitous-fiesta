
def mumbling(s):
  return '-'.join([(l*i).capitalize() for l,i in zip(s,range(1,len(s)+1))])

