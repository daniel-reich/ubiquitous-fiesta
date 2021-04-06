
def pad(message):
  if len(message)==140:
    return message
  if len(message)%2==0:
    message+=' l'
  else:
    message+='l'
  while len(message)<140:
    message+='ol'
  return message

