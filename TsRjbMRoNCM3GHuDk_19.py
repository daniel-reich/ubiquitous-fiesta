
def syllabification(word):
  import re
  consonants="[pbtdkgG?fvszSZxhcjmnrly]"
  vowels="[aAeiou]"
  sylnum=[]
  syllables="{consonants}{vowels}{consonants}{consonants}$|{consonants}{vowels}{consonants}$|{consonants}{vowels}$".format(consonants=consonants, vowels=vowels)
  while len(word)>2:
    syllable=re.findall(syllables,word)[0]
    sylnum.insert(0,syllable)
    word=word[0:len(word)-len(syllable)]
  print(word)
  sylnum.insert(0,".".join(re.findall(syllables,word)))
  print(re.findall(syllables,word))
  return ".".join(sylnum).strip(".")

