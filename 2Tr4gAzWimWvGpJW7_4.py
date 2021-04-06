
def is_there_consecutive(lst, n, times):
  if times > len(lst) or lst == [1]:
    return False
  else:
    row = []
    ap = ''
    for i in lst:
      if i == n:
        ap += str(n)
      else:
        row.append(ap)
        ap = ''
    return len(max(row)) == times

