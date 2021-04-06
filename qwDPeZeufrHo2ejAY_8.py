
def eval_algebra(eq):
  words = eq.split()
  result = 0
  w0 = words[0]
  w1 = words[1] 
  w2 = words[2]
  w3 = words[3] 
  w4 = words[4]
  
  if w0 == "x" and w1 == "+":
    result = int(w4) - int(w2)
  elif w2 == "x" and w1 == "+":
    result = int(w4) - int(w0)
  elif w4 == "x" and w1 == "+":
    result = int(w0) + int(w2)
​
  elif w0 == "x" and w1 == "-":
    result = int(w4) + int(w2)
  elif w2 == "x" and w1 == "-":
    result = (int(w4) - int(w0)) * -1
  elif w4 == "x" and w1 == "-":
    result = int(w0) - int(w2)
​
  return result

