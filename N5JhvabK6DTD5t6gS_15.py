
import string
def markdown(symb):
  def func(sentence, word):
    return ' '.join([symb+w+symb if w.lower().translate(str.maketrans('', '', string.punctuation)) == word.lower() else w for w in sentence.split(' ')])
  return func

