
def hacker_speak(txt):
  hack = {"a":"4","e":"3","i":"1","o":"0","s":"5"}
  return("".join([hack[c] if c.lower() in hack else c for c in txt]))

