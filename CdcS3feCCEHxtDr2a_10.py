
def clear_ordering(lst):
  beginns,ends=[],[]
  for elem in lst:
    beginns.append(elem[0])
    ends.append(elem[1])
  return len(set(beginns))== len(beginns) and len(set(ends))== len(ends)

