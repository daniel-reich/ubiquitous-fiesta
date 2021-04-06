
def alternate_sort(lst):
  a,n = sorted(i for i in lst if type(i)==str),sorted(i for i in lst if type(i)==int)
  return sum([[j,i] for i,j in zip(a,n)],[])

