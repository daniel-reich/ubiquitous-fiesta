
def pad(message):
  if len(message) % 2 == 0:
    if len(message) == 140:
      return message
    message += ' l'
    while len(message) < 140:
      if len(message + 'olololol') > 140:
        while len(message) <= 140:
          if len(message + 'ol') > 140:
            return message
          else:
            message += 'ol'
        return message
      else:
        message += 'olololol'
    return message 
  else:
    message += 'l'
    while len(message) < 140:
      if len(message + 'olololol') > 140:
        while len(message) <= 140:
          if len(message + 'ol') > 140:
            return message
          else:
            message += 'ol'
        return message
      else:
        message += 'olololol'
    return message

