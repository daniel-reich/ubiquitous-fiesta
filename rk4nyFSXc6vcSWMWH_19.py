
def shared_digits(lst):
  out = []
  for i in range(len(lst) - 1):
    if set(str(lst[i])).isdisjoint(set(str(lst[i+1]))):
      out.append(False)
    else:
      out.append(True)
  return all(out)

