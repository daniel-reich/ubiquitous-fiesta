
def letters(word1, word2):
  def to_str(s):
    return "".join(sorted(list(s)))
  word1 = set(list(word1))
  word2 = set(list(word2))
  return [to_str(word1&word2), to_str(word1-word2), to_str(word2-word1)]

