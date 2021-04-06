
def no_yelling(phrase):
  lenPh = len(phrase) - 1
  cnt = 0
  while lenPh > 0:
    if phrase[lenPh] is '?' or phrase[lenPh] is '!':
      cnt += 1
      lenPh -= 1
    else:
      break
  newVal = (len(phrase) - cnt) + 1
  return(phrase[:newVal])

