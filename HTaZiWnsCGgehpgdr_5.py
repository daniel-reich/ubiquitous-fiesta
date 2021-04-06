
def license_plate(s, n):
  s = ''.join(ch for ch in s[::-1].upper() if ch.isalnum())
  return '-'.join(s[i:i+n] for i in range(0, len(s), n))[::-1]

