
def safecracker(start, increments):
  a = increments[0]
  b = increments[1]
  c = increments[2]
  f_list = []
  if start < a:
    start += 100
  f_list.append(start - a)
  start = start - a
  if start + b > 100:
    start -= 100
  f_list.append(start + b)
  start = start + b
  if start < c:
    start += 100
  f_list.append(start - c)
  start = start - c
  return f_list

