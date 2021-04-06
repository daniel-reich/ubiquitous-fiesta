
def edabit_in_string(txt):
  word="edabit"
  new=""
  c=0
  for i in range(len(word)):
    while True:
      if c>=len(txt):
        return "NO"
      if word[i]==txt[c]:
        new+=txt[c]
        c+=1
        break
      c+=1
  if word==new:
    return "YES"
  else:
    return "NO"

