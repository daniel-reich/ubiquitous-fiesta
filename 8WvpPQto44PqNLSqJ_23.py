
def pad(message):
  if len(message) < 140:
    if len(message) % 2 == 0:
      return message + " l" + "ol" * int((140 - 2 - len(message))/2)
    return message + "l" + "ol" * int((140 - 1 - len(message))/2)
  return message

