
def every_some(test, val, a, b, c, d, e):
  
  Sentence_A = str(a) + str(test)
  Test_A = eval(Sentence_A)
  
  Sentence_B = str(b) + str(test)
  Test_B = eval(Sentence_B)
  
  Sentence_C = str(c) + str(test)
  Test_C = eval(Sentence_C)
  
  Sentence_D = str(d) + str(test)
  Test_D = eval(Sentence_D)
  
  Sentence_E = str(e) + str(test)
  Test_E = eval(Sentence_E)
  
  Events = 0
  
  if (Test_A):
    Events += 1
  elif (Test_B):
    Events += 1
  elif (Test_C):
    Events += 1
  elif (Test_D):
    Events += 1
  elif (Test_E):
    Events += 1
    
  if (val == "everybody") and (Events == 5):
    return True
  elif (val == "somebody") and (Events > 0):
    return True
  else:
    return False

