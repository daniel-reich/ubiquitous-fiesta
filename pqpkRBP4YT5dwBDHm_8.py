
def show_the_love(lst):
  m,n=min(lst),sum(lst)/4
  return [.75*x+n if x==m else .75*x for x in lst]

