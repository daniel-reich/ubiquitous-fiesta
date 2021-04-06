
def count_digits(lst, t):
  res = []
  if t=="even":
    for num in lst:
      res.append(sum(1 for ch in str(num) if int(ch)%2==0))
  else:
    for num in lst:
      res.append(sum(1 for ch in str(num) if int(ch)%2==1))
  return res

