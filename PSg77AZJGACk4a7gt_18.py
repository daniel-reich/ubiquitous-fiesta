
def meme_sum(a, b):
  larger = a if len(str(a)) >= len(str(b)) else b
  smaller = b if len(str(a)) >= len(str(b)) else a
  res = []
  for i in range(0, len(str(smaller))):
    res.append(int(str(smaller)[len(str(smaller)) - i - 1]) + int(str(larger)[len(str(larger)) - i - 1]))
  for i in range(len(str(larger)) - len(str(smaller)) - 1, -1, -1):
    res.append(int(str(larger)[i]))
  res = res[::-1]
  return int("".join([str(el) for el in res]))

