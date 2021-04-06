
def loves_me(n):
  lmlmn = ['Loves me' + (' not' if i%2 else '') for i in range(n-1)]
  lmlmn.append('LOVES ME' + (' NOT' if n%2==0 else ''))
  return ', '.join(lmlmn)

