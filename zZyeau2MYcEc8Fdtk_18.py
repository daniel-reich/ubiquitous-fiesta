
def round_number(num, n):
  return num//n*n if num-num//n*n<n//2 else num//n*n+n

