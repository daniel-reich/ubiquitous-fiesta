
def edit_words(lst):
  return [change(w) for w in lst]
​
def change(word):
  word = word.upper()[::-1]
  n = (len(word)+1)//2
  return word[:n] + '-' + word[n:]

