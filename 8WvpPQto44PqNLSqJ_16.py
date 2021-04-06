
def pad(message):
  if len(message)<140:
    if not len(message)%2:
      message += ' l'
    else:
      message += 'l'
    while len(message)<140:
      message += 'ol'
  return message

