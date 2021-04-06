
def reverse_words(words):
  wordlist=words.split()
  answ = ''
  for i in range(len(wordlist)):
    answ = answ + wordlist[len(wordlist)-i-1] + " "
  return answ[:-1]

