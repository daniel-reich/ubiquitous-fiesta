
def mumbling(s):
  a = s.lower()
  return "-".join(a[i].upper()+a[i]*i for i in range(len(a)))

