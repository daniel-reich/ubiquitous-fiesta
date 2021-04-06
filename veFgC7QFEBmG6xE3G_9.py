
def is_smooth(sentence):
  new=[]
  sentence = sentence.lower().split()
  for i in range(len(sentence)-1):
    if sentence[i][-1] == sentence[i+1][0]:
      new.append(sentence[i][-1])
    elif sentence[i][-1] != sentence[i+1][0]:
      return False
      
  return len(new)>0

