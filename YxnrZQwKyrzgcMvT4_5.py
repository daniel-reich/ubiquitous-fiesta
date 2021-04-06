
def rotate_transform(lst, num):
  if num>0:
    c=0
    while c<num:
      lst=[list(x)[::-1] for x in zip(*lst)]
      c+=1
    return lst
  else:
    c=0
    while c<abs(num):
      lst=[list(x) for x in zip(*lst)][::-1]
      c+=1
    return lst

