
def nearest_element(n, lst):
  return lst.index(
    min(
      ((abs(l - n), l) for l in lst), key=lambda i: (i[0], -i[1])
    )[-1]
  )

