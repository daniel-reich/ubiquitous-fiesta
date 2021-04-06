
def format_num(n):
  result = list()
  n = str(n)[::-1]
  while n:
    result.append(n[:3])
    n = n[3:]
  return ",".join(result)[::-1]

