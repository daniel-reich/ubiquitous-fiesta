
def x_pronounce(sentence):
  arr = []
  
  for w in sentence.split():
    output = ""
    if w[0] == 'x' and len(w) != 1:
        output += 'z'
    elif len(w) == 1 and w == 'x':
      output += "ecks"
    else : output += w[0]
    for c in w[1:]:
      if c == 'x':
        output += "cks"
      else : output += c
    arr.append(output)
  return " ".join(arr)

