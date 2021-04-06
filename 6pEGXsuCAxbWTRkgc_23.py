
def loves_me(n):
  love_lst = ["Loves me" if i % 2 == 0 else "Loves me not" for i in range(0, n)]
  love_lst[-1] = love_lst[-1].upper()
  return ', '.join(love_lst)

