
def cap_space(txt):
  return ''.join(' '+ch if ch.isupper() else ch for ch in txt).lower()

