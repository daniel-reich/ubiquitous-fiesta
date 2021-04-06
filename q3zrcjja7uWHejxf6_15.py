
def negative_sum(chars):
  chars = [i for i in chars]
  res = "-0123456789"
​
  for i in range(len(chars)):
    if chars[i] not in res:
      chars[i] = " "
  return sum([eval(i) for i in "".join(chars).split(" ") if "-" in i])

