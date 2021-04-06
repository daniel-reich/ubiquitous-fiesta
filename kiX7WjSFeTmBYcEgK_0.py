
def major_sum(lst):
  pos, neg, zero = 0, 0, 0
  for n in lst:
    if n > 0:
      pos += n
    elif n < 0:
      neg += n
    else:
      zero += 1
  return max(pos, neg, zero, key=abs)

