
def strong_password(p):
  n = "0123456789"
  l = "abcdefghijklmnopqrstuvwxyz"
  u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  s = "!@#$%^&*()-+"
  no_n = not [0 for i in p if i in n]
  no_l = not [0 for i in p if i in l]
  no_u = not [0 for i in p if i in u]
  no_s = not [0 for i in p if i in s]
  return max(no_n + no_l + no_u + no_s, 6 - len(p))

