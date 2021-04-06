
def cleave(string, lst, rec_call=False):
  possible_words = []
  for ref_word in lst:
    if string[:min(len(string), len(ref_word))] == ref_word:
      if(len(string) == len(ref_word)):
        return string
      possible_words.append(ref_word)
  for word in possible_words:
    result = cleave(string[len(word):], lst, True)
    if result is not None:
      return word + " " + result
  return None if rec_call else "Cleaving stalled: Word not found"

