
def digit_count(n):
  newlist = []
  x = str(n)
  for eachdigit in x:
    newlist.append(str(x.count(eachdigit)))
  return int(''.join(newlist))

