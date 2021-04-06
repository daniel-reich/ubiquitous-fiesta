
def is_sastry(n):
  concat = int(str(n) + str(n+1)) ** 0.5
  return concat == int(concat)

