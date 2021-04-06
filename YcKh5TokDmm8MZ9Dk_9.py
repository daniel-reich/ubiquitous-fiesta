
def hidden_anagram(text, phrase):
  text = [i for i in text.lower() if i.isalpha()]
  phrase = [i for i in phrase.lower() if i.isalpha()]
  for i in range(len(text)-len(phrase)+1):
    if all([x in phrase and phrase.count(x)==text[i:i+len(phrase)].count(x) for x in text[i:i+len(phrase)]]):
      return ''.join(text[i:i+len(phrase)])
  return 'noutfond'

