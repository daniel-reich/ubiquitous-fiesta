
def consonants(word):
  s=""
  v="aeoui"
  co=0
  for x in word.lower():
    if x.isalpha():
      if x not in v:
        co+=1
  return co
def vowels(word):
  s=""
  v="aeoui"
  vo=0
  for x in word.lower():
    if x.isalpha():
      if x in v:
        vo+=1
  return vo

