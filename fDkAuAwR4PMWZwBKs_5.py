
def find_bob(n):
​
  try:
    return n.index('Bob')
​
  except ValueError:
    return -1

