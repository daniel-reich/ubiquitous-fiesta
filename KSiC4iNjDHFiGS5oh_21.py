
def is_super_d(n):
  for i in range(2, 10):
    t = i * (n ** i)
    s = i * (str(i))
    if s in str(t):
      return 'Super-' + str(i) + " Number"
  return "Normal Number"

