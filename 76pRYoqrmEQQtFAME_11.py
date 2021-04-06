
def is_astonishing(num):
  numstr = str(num)
  for i in range(1, len(numstr)):
    left = int(numstr[:i])
    right = int(numstr[i:])
    res = ((right - left + 1) / 2) * (left + right) if left < right else ((left - right + 1) / 2) * (right + left)
    if res == num:
      return "AB-Astonishing" if left < right else "BA-Astonishing"
  return False

