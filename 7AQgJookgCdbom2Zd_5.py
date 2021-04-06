
#Move the first letter of each word to the end of the word.
#Add "ay" to the end of the word.
#Words starting with a vowel (A, E, I, O, U) simply have "WAY" appended to the end.
​
lv = "aeiou"
uv = "AEIOU"
​
def piglatinize_word(word):
  if word=="": return ""
  y = ""
  capital = word[0].isupper()
  starting_with_v = word[0] in lv+uv
  if starting_with_v: y+=word[0]
  y += word[1:]
  if starting_with_v: y+="way"
  else: y+=word[0]+"ay"
  if capital: y = y.capitalize()
  return y
​
def pig_latin(txt):
  y = ""
  send = ""
  for c in txt:
    if c.isalpha(): send += c
    else:
      y += piglatinize_word(send)
      send = ""
      y += c
  return y

