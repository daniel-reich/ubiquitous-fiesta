
def no_strangers(txt):
  txt2 = ""
  
  for letter in txt:
    if letter.isalpha() or letter == " " or letter == "'":
      txt2 += letter.lower()
      
  lst = txt2.split()
  
  friends = []
  acquaintances = []
  strangers = {}
  result = []
  
  for l in lst:
    if not l in strangers.keys():
      strangers[l] = 1
    else:
      strangers[l] = strangers[l] + 1
      if strangers[l] == 3:
        acquaintances.append(l)
      elif strangers[l] == 5:
        acquaintances.pop(acquaintances.index(l))
        friends.append(l)
  
  result.append(acquaintances)
  result.append(friends)
  return result

