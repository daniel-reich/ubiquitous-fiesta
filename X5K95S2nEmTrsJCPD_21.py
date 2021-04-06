
def emotify(txt):
  emotes = {"smile": ":D", "grin": ":)", "sad": ":(", "mad": ":P"}
  words = txt.split(' ')
  emotion = words[-1]
  face = ''
  
  for key in emotes.keys():
    if emotion == key:
      face = emotes[emotion]
  return "Make me " + face

