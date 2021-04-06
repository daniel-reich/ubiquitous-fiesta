
def is_smooth(sentence):
  result = True
  
  words = sentence.split(" ")
  for i in range(len(words) - 1):
    if words[i][-1].lower() != words[i + 1][0].lower():
      result = False
  
  return result

