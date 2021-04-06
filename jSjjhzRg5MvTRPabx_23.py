
def sentence(words):
  sentence = ", ".join(("a " if not w[0] in "aeiou" else "an ") + w for w in words)
  for ix in range(len(sentence) - 1, -1, -1):
    if sentence[ix] == ",":
      break
  return "A{} and{}.".format(sentence[1:ix], sentence[ix+1:])

