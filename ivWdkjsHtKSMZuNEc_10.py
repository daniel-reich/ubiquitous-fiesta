
import re
​
def find_shortest_words(txt):
  print(txt.split())
  words = txt.split()
  words_letters = []
  shortest_word_length = 100
  short_words =[]
  
  for word in words:
    words_letters.append(re.sub('[^a-zA-Z]', '', word).lower())
  words_letters = list(filter(None, words_letters))
  print(words_letters)
  
  for word in words_letters:
    print(word, len(word))
    if len(word) < shortest_word_length:
      shortest_word_length = len(word)
      short_words = [word]
    elif len(word) == shortest_word_length:
      short_words.append(word)
  print(sorted(short_words))
  return sorted(short_words)

