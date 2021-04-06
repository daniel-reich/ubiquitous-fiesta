
def correct_sentences(s):
  s = s.strip()
  words = s.split()
  output = []
  
  for a, b in zip(words, words[1:] + [words[0]]):
    if b[0].isupper():
      output.append(a + '.')
    else:
      output.append(a)
      
  sentences = [i.capitalize() for i in ' '.join(output).split('. ')]
  return '. '.join(sentences) + '.'

