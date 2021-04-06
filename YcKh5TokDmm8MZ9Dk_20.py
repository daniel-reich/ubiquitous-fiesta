
def hidden_anagram(text, phrase):
  text = ''.join([i for i in text.lower() if i.isalpha()])
  text_sorted = sorted(text)
  phrase = ''.join([i for i in phrase.lower() if i.isalpha()])
  phrase_sorted = sorted(phrase.lower())
  anagram = []
  
  for n, c in enumerate(phrase_sorted):
    if phrase_sorted[n] == c:
      anagram.append(c)
  length = len(anagram)
  for i in range(len(text_sorted) - length + 1):
    substr = text[i:i+length]
    if sorted(substr) == anagram:
      return substr
  return "noutfond"

