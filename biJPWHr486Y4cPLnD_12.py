
def chunkify(lst, size):
  output = []
  while len(lst) > 0:
    output.append(lst[:size])
    lst = lst[size:]
  return output

