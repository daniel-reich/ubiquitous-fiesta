
def pad(message):
  if len(message)==140: return message
  if len(message)%2:  return message+("lo"*((140-(len(message)+1))//2))+"l"
  else: return message+" "+("lo"*((140-(len(message)+2))//2))+"l"

