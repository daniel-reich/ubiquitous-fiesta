
def truncate(txt, length):
  rawr = txt.split()
  sum = 0
  ans = []
  for x in rawr:
    if len(x) + sum <= length:
      ans.append(x)
      print (sum)
      sum += len(x) + 1
      print(sum)
    else:
      sum += 99999
  return (' '.join(ans))

