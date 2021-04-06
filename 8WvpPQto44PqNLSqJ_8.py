
def pad(message):
  if len(message) % 2 == 0:
    message += " "
  while len(message) < 140:
    message += "lo"
  return message[:len(message)-1]

