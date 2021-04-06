
def strong_password(p):
  strength = 0
  if any(ch.islower() for ch in p): strength += 1
  if any(ch.isupper() for ch in p): strength += 1
  if any(ch.isdigit() for ch in p): strength += 1
  if any(ch in '!@#$%^&*()-+' for ch in p): strength += 1
  req = 4 - strength
  return max(req,6-len(p))

