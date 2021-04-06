
def pad(message):
  l=len(message)
  if l<140:
    if l%2:
      return message+'lo'*((140-l-1)//2)+'l'
    else:
      return message+' '+'lo'*((140-l-2)//2)+'l'
  else:
    return message

