
def automorphic(n):
  sqr_num = n ** 2
  return n == int(str(sqr_num)[-len(str(n)):])

