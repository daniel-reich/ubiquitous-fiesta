
def x_pronounce(sentence):
  s = sentence.split()
  new_sentence = ""
  for word in s:
    if word == 'x':
      new_sentence += 'ecks '
    elif word[0] == 'x':
      new_sentence += 'z' + word[1:] + " "
    elif 'x' in word:
      new_sentence += word.replace('x','cks') + " "
    else:
      new_sentence += word + " "
  return new_sentence.rstrip()

