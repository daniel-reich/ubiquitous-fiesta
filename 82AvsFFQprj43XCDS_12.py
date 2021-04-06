
def no_strangers(txt):
  bad_chars = ',".'
​
  for c in bad_chars: txt = txt.replace(c, "").lower()
  words = [word for word in txt.split(" ")]
  count_map = {word: 0 for word in set(words)}
  
  aqs = []
  frds = []
  for word in words:
    count_map[word] += 1
    
    if count_map[word] == 3:
      aqs.append(word)
    elif count_map[word] == 5:
      aqs.pop(aqs.index(word))
      frds.append(word)
  return [aqs, frds]

