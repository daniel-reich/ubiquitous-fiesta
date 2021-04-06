
def char_index(word, char):
  if char in word: ans=[word.index(char),0]
  else: return None
  for i in range(len(word)):
    if word[i]==char:
      ans[1]=i
  return ans

