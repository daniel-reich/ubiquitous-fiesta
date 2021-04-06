
def sentence(words):
  words = ["an "+ w if w[0] in "aeiou" else "a "+ w for w in words]
  return "{} and {}.".format(", ".join(words[:-1]).capitalize(), words[-1])

