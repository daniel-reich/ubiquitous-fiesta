
import re
​
def replacer(match_obj):
  output = match_obj.group(3)
  if match_obj.group(2) != "":
    if match_obj.group(2)[0].isupper():
      output = output.capitalize()
    output += match_obj.group(2).lower()
  else:
    output += "y"
  return match_obj.group(1) + output + "ay" + match_obj.group(4)
​
def translate_word(word):
  return re.sub("^([^a-zA-Z]*)([^AaEeIiOoUu]*)([a-zA-Z]+)(.*)$", replacer, word)
​
def translate_sentence(sentence):
  return " ".join(translate_word(word) for word in sentence.split(" "))

