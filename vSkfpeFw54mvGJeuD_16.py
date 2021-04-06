
def lychrel(n):
  for i in range(500):
    n_lst = list(str(n))
    if n_lst == n_lst[::-1]:
      return i
    n += int(''.join(n_lst[::-1]))
  return True

