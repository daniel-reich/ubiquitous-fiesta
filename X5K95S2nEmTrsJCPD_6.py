
def emotify(txt):
  emotes = {"smile":":D","grin":":)","sad":":(", "mad":":P"}
  return ' '.join(emotes[t] if t in emotes else t for t in txt.split())

