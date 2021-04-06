
def shared_letters(txt1, txt2):
  print(txt1,"|" , txt2)
  same_letters = []
  for i in range(0, len(txt1)):
    if txt1[i] in txt2 and txt1[i] not in same_letters:
      same_letters.append(txt1[i])
      
  return len(same_letters)

