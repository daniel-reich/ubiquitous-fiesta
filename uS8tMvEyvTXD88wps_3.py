
def reverse(txt):
  output=[]
  for word in txt.split():
    if len(word) < 5:
      output.append(word)
    else:
      output.append(word[::-1])
  return " ".join(output)

