
def license_plate(s, n):
  s = s.replace('-', '').upper()
  lst = []
  for i in range(len(s), 0, -n):
    lst.insert(0, s[max(0, i-n):i])
  return '-'.join(lst)

