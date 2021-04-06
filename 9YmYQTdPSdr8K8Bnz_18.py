
def unique_lst(lst):
  l=[i for i in lst if i>0]
  ul=[]
  for i in l:
    if i not in ul:
      ul.append(i)
  return ul

