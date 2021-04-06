
def is_astonishing(num):
  num = str(num)
  for i in range(1, len(num)):
    prev_a = int(num[:i])
    prev_b = int(num[i:])
    a, b = (prev_b, prev_a) if prev_a > prev_b else (prev_a, prev_b)
    sum_ab = (b * (b + 1) / 2) - (a**2 - a) / 2
    if sum_ab == int(num):
      return "AB-Astonishing" if prev_a < prev_b else "BA-Astonishing"
  return False

