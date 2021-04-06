
def find_longest(sentence):
  words = sentence.split()
  longest = 0
  longest_word=''
  for i in words:
    length = 0
    for j in i:
      if j.isalpha():
        length+=1
    if length>longest:
        longest = length
        longest_word=i
  return_word = ''
  for i in longest_word:
    if i.isalpha():
      return_word+=i
    else:
      break
  
  return return_word.lower()

