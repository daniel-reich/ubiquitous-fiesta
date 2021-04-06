
def is_smooth(sentence):
  sentence = sentence.lower()
  var = sentence.split()
  a = len(var)
  counter = 0
  for i in range(0, a):
    if i != a - 1:
      c = var[i] [-1]
      d = var[i+1] [0]
      if c == d:
        counter = counter + 1
  return counter == len(var) - 1

