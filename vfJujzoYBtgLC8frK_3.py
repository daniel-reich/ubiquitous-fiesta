
def word_to_decimal(word):
  word = word.lower()
  a = ' abcdefghijklmnopqrstuvwxyz'
  mx = max([a.index(i) for i in word])+10
  return sum([(a.index(word[i])+9)*(mx**(len(word)-i-1)) for i in range(len(word))])

