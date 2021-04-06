
def numbers_to_ranges(lst):
  d=0
  lst2=[]
  if len(lst)==0:
    return []
  if len(lst)==1:
    return [str(i) for i in lst]
  while d<=len(lst)-1:  
      start=lst[d]
      while lst[d]+1==lst[d+1]:
          d+=1
          if d==len(lst)-1:
              break
      if start==lst[d]:
          lst2.append('{}'.format(start))
      else:
          lst2.append('{}-{}'.format(start,lst[d]))
      d+=1
  return lst2

