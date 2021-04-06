
def pig_latin_sentence(sentence):
  words = sentence.split()
  vowels = 'aeiou'
  for i in range(len(words)):
    if words[i][0] in vowels:
      words[i] = words[i] + 'way'
    else:
      while words[i][0] not in vowels:
        words[i] = words[i][1:] + words[i][0]
      words[i] += 'ay'
  return ' '.join(words)

