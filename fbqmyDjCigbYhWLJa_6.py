
def split_into_buckets(ph, n, B=[]):
  if n >= len(ph):
    return B + [ph]
  if " " not in ph[:n+1]:
    return []
  k = ph[:n+1].rindex(" ")
  return split_into_buckets(ph[k+1:], n, B + [ph[:k]])

