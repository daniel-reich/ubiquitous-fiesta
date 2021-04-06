
def true_alphabetic(txt):
  def word_length_finder(word):
    return len(word)
  def word_maker(string, lengths):
    words = []
    string = list(string)
    for length in lengths:
      word = ''
      for n in range(length):
        word += string[0]
        string.pop(0)
      words.append(word)
    return words
  
  words = txt.split()
  word_lengths = []
  
  for word in words:
    word_lengths.append(word_length_finder(word))
  
  rawstring = sorted(''.join(words))
  string = ''
  
  for item in rawstring:
    string += item
  
  new_words = word_maker(string, word_lengths)
  
  return ' '.join(new_words)

