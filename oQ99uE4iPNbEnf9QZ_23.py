
def no_perms_digits(n):
  sam = 1
  for i in range(n,0,-1):
    sam = sam * i
  return len(str(sam))

