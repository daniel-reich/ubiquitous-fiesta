
def chunkify(lst, size):
  out = []
  while len(lst) > size:
    out.append(lst[:size])
    lst = lst[size:]
  out.append(lst)
  return out

