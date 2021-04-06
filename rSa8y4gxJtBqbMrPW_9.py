
def lcm(n1, n2):
  n_multiple = set()
  i = 1
  while True:
      if n1*i not in n_multiple:
          n_multiple.add(n1*i)
      else:
          return n1*i
​
      if n2*i not in n_multiple:
          n_multiple.add(n2*i)
      else:
          return n2*i
​
      i += 1

