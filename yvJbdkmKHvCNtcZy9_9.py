
def is_disarium(n):
  s = 0
  for i in str(n):
    s += int(i)**(str(n).index(i) + 1)
  return s == n

