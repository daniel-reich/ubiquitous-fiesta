
def pig_latin_sentence(sentence):
  x = sentence.split(" ")
  a = []
  vowel = "aeiou"
  for i in x:
    if i[0] in vowel:
      c = i + "way"
      a.append(c)
    else:
      for j in i :
        if j in vowel:
          p = i.index(j)
          break
      c = i[p::] + i.replace(i[p::], "") + "ay"
      a.append(c)
​
  return " ".join(a)

