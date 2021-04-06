
def steps_to_convert(txt):
  num = 0
  num1 = 0
  for i in txt:
    if(i.isupper()):
      num += 1
    else:
      num1 += 1
  return min([len(txt)-num, len(txt)-num1])

