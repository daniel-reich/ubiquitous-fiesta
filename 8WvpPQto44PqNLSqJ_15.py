
def pad(msg):
  msg = msg[:140] if len(msg)>139 else msg+' ' if not len(msg)%2 else msg
  return msg + ('ol'*70)[len(msg):]

