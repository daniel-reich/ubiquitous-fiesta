
def word_nest(word, nest):
​
  return 0 if word == nest else 1 + word_nest(word,nest.replace(word,''))

