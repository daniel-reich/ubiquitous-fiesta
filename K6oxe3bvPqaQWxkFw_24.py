
def join_digits(n):
  newlist = []
  for eachnumber in range(1,n+1):
    digit = str(eachnumber)
    for eachdigit in digit:
      newlist.append(eachdigit)
  return '-'.join(newlist)

