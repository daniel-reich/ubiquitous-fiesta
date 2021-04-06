
def digits_count(num, s=0):
  if not isinstance(num, str): return digits_count(str(abs(int(num))))
  return digits_count(num[:-1], s=s+1) if num else s

