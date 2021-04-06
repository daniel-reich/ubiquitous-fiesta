
alphabet = 'abcdefghijklmnopqrstuvwxyz'
​
def missing_letter(txt):
  output = []
  for i in alphabet:
    if i > txt[0] and i < txt[-1] and i not in txt:
      output.append(i)
  if len(output) == 0:
    return "No Missing Letter"
  return output[0]

