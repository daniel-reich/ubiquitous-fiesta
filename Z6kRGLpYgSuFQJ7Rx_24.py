
def find_longest(sentence):
  new_sentence = ''
  word_list = []
  letter_count = 0
  longest_word = ''
  sentence = sentence.replace('\'s', '')
  for _ in sentence:
    if _.isalnum() or _ == ' ':
      new_sentence += _
  word_list = list(new_sentence.split())
  for word in word_list:
    if len(word) > letter_count:
      longest_word = word
      letter_count = len(word)
  return longest_word.lower()

