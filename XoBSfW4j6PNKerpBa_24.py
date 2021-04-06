
def complete_factorization(n):
  i = 2
  lst = []
  while i < n:
    while n%i == 0:
      n = n/i
      lst.append(i)
    i = i + 1
  if n != 1:
    lst.append(int(n))
  return(lst)

