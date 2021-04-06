
def is_smooth(sentence):
  sentence = sentence.split(" ")
  x = 0
  for i in range(0, len(sentence)-1):
    if sentence[i][-1].lower() == sentence[i+1][0].lower():
      x += 1
  return x == len(sentence)-1

