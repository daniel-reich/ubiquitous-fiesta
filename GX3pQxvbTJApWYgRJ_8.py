
def is_kaprekar(n):
  sq = n**2
  if len(str(sq)) == 1:
    sq = "0" + str(sq)
  left = int(str(sq)[:len(str(sq))//2])
  right = int(str(sq)[len(str(sq))//2:])
  return (left + right) == n

