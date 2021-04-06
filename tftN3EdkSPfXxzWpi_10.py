
def sentence_searcher(txt, n):
  cur_sentence = []
  index = 0
  text = txt.split()
  n = n % len(text)
  searched_word = text[n]
  for word in text:
    cur_sentence.append(word)
    if word.endswith('.'):
      if index >= n:
        return ' '.join(cur_sentence)
      cur_sentence = []
    index += 1

