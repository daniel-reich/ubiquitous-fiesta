
def latin(word):
  for index, letter in enumerate(word):
    if letter in 'aeiou':
      break
  return word[index:] + word[:index] + 'ay'
​
​
def pig_latin_sentence(sentence):
  return ' '.join(
    word + 'way' if word[0] in 'aeiou' else latin(word)
    for word in sentence.split()
  )

