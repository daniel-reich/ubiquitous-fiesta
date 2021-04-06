
def constraint(txt):
  txt = txt.lower()
  if all([c in txt for c in 'abcdefghijklmnopqrstuvwxyz']):
    return "Pangram"
  if all([txt.count(c) < 2 for c in 'abcdefghijklmnopqrstuvwxyz']):
    return "Heterogram"
  words = txt.split()
  if all([word[0] == words[0][0] for word in words]):
    return "Tautogram"
  common_letters = [c for c in words[0]]
  for word in words:
    common_letters = [c for c in common_letters if c in word]
  if len(common_letters) > 0:
    return "Transgram"
  return "Sentence"

