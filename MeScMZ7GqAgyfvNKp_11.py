
def empty_sq(step):
  
  if (step < 2):
    Answer = 0
    return Answer
  else:
    PreStep1 = step * step
    PreStep2 = PreStep1 - step
    PreStep3 = PreStep2 * 4
    Answer = PreStep3
    return Answer

