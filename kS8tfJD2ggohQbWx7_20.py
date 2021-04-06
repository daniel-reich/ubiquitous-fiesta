
def last_name_lensort(lst):
  return sorted(sorted(lst,key= lambda x: x.split()[-1]),key= lambda x: len(x.split()[-1]))

