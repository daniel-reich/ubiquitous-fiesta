
def is_special_array(l):
  return all(
    i%2 == n%2
    for i, n in enumerate(l)
  )

