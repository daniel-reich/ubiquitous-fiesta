
def num_split(num):
  n = list(str(abs(num)))
  res = [int(n[i])  * int("1" + "0" * (len(n) - i - 1)) for i in range(len(n))]
  return res if num > 0 else [-i for i in res]

