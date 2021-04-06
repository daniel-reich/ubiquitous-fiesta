
def square_patch(n):
  sq_main = []
  sq_inner = []
  for i in range(0, n):
    sq_inner.append(n)
  for i in range(0, n):
    sq_main.append(sq_inner)
  return sq_main

