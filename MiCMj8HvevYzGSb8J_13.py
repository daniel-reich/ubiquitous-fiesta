
def fibo_word(n):
  if n < 2:
    return 'invalid'
  lst = ['b','a']
  while len(lst)<n:
    lst.append(lst[-1]+lst[-2])
  return ', '.join(lst)

