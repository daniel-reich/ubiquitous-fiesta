
def remove_letters(letters, word):
  ans = []
  word = [x for x in word]
  for i in  letters:
    if i in word:
      word.remove(i)
    else:
      ans.append(i)
      
  return ans

