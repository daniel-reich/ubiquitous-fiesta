
sentence01 = "it's a hard knock life"
sentence02 = "a big booty woman"
​
def increasing_word_weights(sentence):
  # compare integer value of each word in a list and returns True if each is greater than the previous
  lst = word_weights(sentence)
  mx = lst[0]
  for i in lst:
    if i > mx:
      mx = i
    elif i < mx:
      break
  return True if [mx] == lst[-1:] else False
​
def word_weights(sentence):
  # Get the value of each character in each word and add them per word.
  words = convert_to_list(sentence)
  ords = []
  word_values = []
  character_value = 0
  word_value = 0
  for i in range(len(words)):
    ords.append(character_value)
    
    for character in words[i]:
      if character.isalpha():
        character_value += ord(character)
    word_value = character_value - ords[i]
    word_values.append(word_value)
  return word_values
​
def convert_to_list(sentence):
  # changes sentence to list, to separate words
  return (sentence.split())

