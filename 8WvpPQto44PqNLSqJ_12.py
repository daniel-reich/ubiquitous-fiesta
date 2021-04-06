
def pad(message):
  if len(message) == 140:
    return message
  if len(message) % 2 == 0:
    message += ' '
  message += 'l'
  message += 'ol' * ((140-len(message))//2)
  return message

