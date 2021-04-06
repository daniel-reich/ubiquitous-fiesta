
def can_build(txt1, txt2):
  canBuild = False
  txt2 = txt2.split(" ")
  for word in txt2:
      if len(word) > 0:
          for i in word:
              if i in txt1:
                  word = word.replace(i, "", 1)
                  txt1 = txt1.replace(i, "", 1)
  for i in txt1:
      if i == " ":
          txt1 = txt1.replace(" ", "")
  if len(txt1) == 0:
      canBuild = True
​
  return canBuild

