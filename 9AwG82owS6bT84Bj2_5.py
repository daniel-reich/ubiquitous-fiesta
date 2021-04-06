
def doubled_pay(n):
  lista=[1]
  n=n-1
  while n>0:
    lista.append(lista[-1]*2)
    n=n-1
  return sum(lista)

