
def char_index(word, char):
  step = [i for i, x in enumerate(word) if x == char]
  if len(step)>0:
    step1 = [step[0],step[-1]]
    return step1
  else:
    return None

