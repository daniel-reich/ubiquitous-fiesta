
def is_astonishing(num):
  n = str(num)
  for i in range(1,len(n)):
    a, b = int(n[:i]), int(n[i:])
    h, l = max(a,b), min(a,b)-1
    if h*(h+1)//2 - l*(l+1)//2 == num:
      if h == b: return 'AB-Astonishing'
      if h == a: return 'BA-Astonishing'
  return False

