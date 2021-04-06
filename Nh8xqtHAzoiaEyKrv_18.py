
def correct_sentences(s):
  words = [el for el in s.split(' ') if len(el) > 0]
  words[0] = words[0].capitalize()
  words[len(words) - 1] += '.'
  for i in range(1,len(words) - 1):
    if words[i + 1][0].isupper():
      words[i] += "."
  return " ".join(words)

