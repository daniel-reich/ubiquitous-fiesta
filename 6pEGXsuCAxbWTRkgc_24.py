
def loves_me(n):
  lst = ["Loves me" if not i%2 else "Loves me not" for i in range(n)] 
  return ', '.join(lst[j].upper() if j == len(lst)-1 else lst[j] for j in range(len(lst)))

