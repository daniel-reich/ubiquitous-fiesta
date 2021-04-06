
def initialize(names):
  new_lst=[]
  for i in names:
    j=i.split()
    k=''
    for name in j:
      k+='{}. '.format(name[0])
    new_lst.append(k)   
  return [i[:-1] for i in new_lst]

