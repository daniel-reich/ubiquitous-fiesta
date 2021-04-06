
def correct_spacing(sentence):
  while "  " in sentence:
    sentence = sentence.replace("  ", " ")
  return sentence.strip()

