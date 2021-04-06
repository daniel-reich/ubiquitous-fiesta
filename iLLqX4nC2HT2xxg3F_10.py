
def deepest(lst):
  lst=''.join(i for i in str(lst) if i in '[]');c=0
  while lst!='':lst=lst.replace('[]','');c+=1
  return c

