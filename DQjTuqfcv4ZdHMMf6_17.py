
def kaprekar(num):
  it = 0
  while num != 6174:
    it += 1
    n1s = str(num)
    while len(n1s) < 4:
      n1s += "0"
    n1s = "".join(sorted(list(n1s)))
    n2s = n1s[::-1]
    num = abs(int(n1s)-int(n2s))
  return it

