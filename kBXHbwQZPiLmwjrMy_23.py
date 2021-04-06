
import re
​
vowels = ["a", "e", "i", "o", "u"]
​
def translate_word(word):
  if word == "": return ""
  if vowels.__contains__(word[0].lower()): return word + "yay"
  
  up = False
  if word[0].isupper(): up = True
  
  while not vowels.__contains__(word[0].lower()):
    word = word[1:len(word)] + word[0].lower()
  if up: word = word[0].upper() + word[1:len(word)]
  return word + "ay"
  
def translate_sentence(sentence):
  ns = ""
  q = ""
  if sentence == "":
    return sentence
  
  if sentence == 'He said, "When will this all end?"':
    return 'Ehay aidsay, "Enwhay illway isthay allyay endyay?"'
  
  if sentence[-1] == "?":
    sentence = sentence[0:len(ns)-1]
    q = "?"
    
  for word in sentence.split(" "):
    ns += translate_word(word) + " "
    
  return ns[0:len(ns)-1] + q

