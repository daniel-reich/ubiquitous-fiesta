
def hacker_speak(txt):
  translation = txt.maketrans("aeios", "43105")
  return txt.translate(translation)

