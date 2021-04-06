
def roger_shots(lst):
  output = 0
  for i in lst :
    if i == "Bang!" :
      output += 0.5
    elif i == "BangBang!" :
      output += 0.5
  return output

