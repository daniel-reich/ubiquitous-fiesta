
def mult_table(n):
  t = [list(range(1, n+1))]
  # for x in range(2, n+1):
    # l = [x]
    # for y in t[0][1:]:
      # l += [x * y]
    # t += [l]
  # return t
  
  return t + [[x] + [y * x for y in t[0][1:]] for x in range(2, n+1)]

