
def merge_arrays(a, b):
  lst = []
  if len(a) < len(b):
    i = 0
    for i in range(0, len(a)):
      lst.append(a[i])
      lst.append(b[i])
      i += 1
    for j in range(0, len(b) - len(a)):
      lst.append(b[i])
      i += 1
    return lst
  if len(b) < len(a):
    i = 0
    for i in range(0, len(b)):
      lst.append(a[i])
      lst.append(b[i])
      i += 1
    for j in range(0, len(a) - len(b)):
      lst.append(a[i])
      i += 1
    return lst
  else:
    for i in range(0, len(a)):
      lst.append(a[i])
      lst.append(b[i])
  return lst

