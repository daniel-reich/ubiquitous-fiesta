
def mubashir_function(a, b):
  check = all(n > 9 for n in [a, b])
  plus = max(a, b)
  minus = min(a, b)
  rslt = a * b
  return int(str(rslt)[0]) if check and a == b else int(str(minus)[::-1]) if check and plus > minus else rslt

