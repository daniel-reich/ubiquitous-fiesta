
def pad(message):
  c = 'ol'
  if len(message) >= 140:
    return message
  if len(message) % 2 == 0:
    message = message + ' l'
  else:
    message = message + 'l'
  while len(message) < 140:
    message = message + c
  return message

