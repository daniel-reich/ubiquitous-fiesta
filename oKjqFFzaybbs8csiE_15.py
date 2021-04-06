
def cons(lst):
  maximo=max(lst)
  minimo=min(lst)
  lista=list(range(minimo,maximo+1))
  return lista==sorted(lst)

