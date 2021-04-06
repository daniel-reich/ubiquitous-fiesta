
def s(a, b):
  return (a + b) * (b - a + 1) // 2
​
def is_astonishing(num):
  n = str(num)
  for i in range(1, len(n)):
    a, b = int(n[:i]), int(n[i:])
    if s(a, b) == num:
      return "AB-Astonishing"
    if s(b, a) == num:
      return "BA-Astonishing"
  return False

