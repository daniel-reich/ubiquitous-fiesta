
def remove_leading_trailing(n):
  res = str(float(n))
  return res[:-2] if res.endswith('.0') else res

