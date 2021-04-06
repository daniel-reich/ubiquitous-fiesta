
def license_plate(s, n):
  s = s.replace('-','').upper()
  final = []
  for i in range(len(s),0,-n):
    if i-n>=0:
      final.append(s[i-n:i])
  extra = s[:len(s)%n]
  return '-'.join([extra]+final[::-1]) if extra!='' else '-'.join(final[::-1])

