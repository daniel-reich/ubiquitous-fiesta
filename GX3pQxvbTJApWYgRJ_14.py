
def is_kaprekar(n):
  if n in [0,1] or all(d == '9' for d in str(n)):
    return True
  else:
    sq = str(n**2)
    left = 0 if len(sq) in [1, 3] else int(sq[:len(sq)//2])
    right = int(sq[len(sq)//2:])
    return left + right == n

