
def same_letter_pattern(txt1, txt2):  
  if (standardize(txt1) == standardize(txt2)):
    return True
  return False
​
def standardize(txt):
  workedOnLetters = []
  currentStandardIdx = 0;
  baseText = list(txt)
​
  for idx in range(len(baseText)):
    currentLetter = baseText[idx] 
​
    foundLetterPreviously = False
    previousLetterIdx = 0
    for previousLetter in workedOnLetters:
      if previousLetter == currentLetter:
        foundLetterPreviously = True
        baseText[idx] = previousLetterIdx;
        break
      previousLetterIdx += 1
    
    if foundLetterPreviously == False:
      workedOnLetters.append(currentLetter)
      baseText[idx] = currentStandardIdx;
      currentStandardIdx += 1
    
  return "".join(map(str, baseText))

