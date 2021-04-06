
def can_complete(initial, word):
  new_initial = [i for i in initial]
  new_word = [i for i in word]
​
  space_left = len(new_word) - len(new_initial)
  for i in range(1,space_left+1):
    new_initial+=[" "]
 
  j = 0 
  for i in new_initial:
    if j >= len(new_word):
      break
    else: 
      if i != new_word[j]:
        new_initial.insert(j, new_word[j])
      j+=1
​
  join_back = "".join(new_initial).strip()
​
  if join_back == word:
    return True
  else:
    return False

