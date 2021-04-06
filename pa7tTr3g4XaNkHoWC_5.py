
def pig_latin_sentence(string):
  string = string.split()
  lst = []
  for word in string:
    if word[0] in "aeiou":
      word = word + "way"
      lst.append(word)
    else:
      for letter in word:
        if letter in "aeiou":
          word = list(word)
          word = word[word.index(letter):] + word[:word.index(letter)]
          word = "".join(word) + "ay"
          lst.append(word)
          break
​
  lst = " ".join(lst)
  return lst

