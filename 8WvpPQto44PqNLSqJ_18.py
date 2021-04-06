
def pad(message):
  l = len(message)
  if l >= 140:
    return message[:140]
    
  rem = 140 - l
  if l % 2 == 0:
    return message + " l" + ("ol" * ( (rem - 2) // 2) )
  else:
    return message + "l" + ("ol" * (rem // 2) )

