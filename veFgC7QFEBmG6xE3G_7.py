
def is_smooth(sentence):
  words = sentence.split(" ")
  for i in range(len(words)-1):
    if words[i][-1] != words[i+1][0].lower():
      return False
  return True

