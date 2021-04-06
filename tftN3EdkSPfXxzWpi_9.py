
def sentence_searcher(txt, n):
  words = txt.split()
  i_start = i_end = n if n >= 0 else len(words) + n
  while not words[i_end].endswith('.'):
    i_end += 1
  while i_start > 0 and not words[i_start - 1].endswith('.'):
    i_start -= 1
  return ' '.join(words[i_start:i_end + 1])

