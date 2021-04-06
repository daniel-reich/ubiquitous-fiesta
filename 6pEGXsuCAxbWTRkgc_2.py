
def loves_me(n):
  lst = [['Loves me', 'Loves me not'][i%2] for i in range(n)]
  lst[-1] = lst[-1].upper()
  return ', '.join(lst)

