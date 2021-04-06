
def retrieve(txt):
  try:
    vowels = ["A", "E", "I", "O", "U", "a","e","i","o","u"]
    txtlst = txt.split(" ")
    newlst = []
    for word in txtlst:
      if word[0] in vowels:
        newlst.append(word.lower().strip("."))
    return newlst
  except:
    return []

