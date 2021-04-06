
def pig_latin_sentence(sentence):
  pig_latin_lst = []
  
  #Seperation of words
  words = sentence.split(" ")
  
  #Vowels
  vowel = ['a', 'e', 'i', 'o', 'u']
  
  #Loop for pig latin
  for x in words:
    if x[0] in vowel:
      pig_latin_lst.append(x+"way")
    else:
      for i in range(len(x)):
        if x[i] in vowel:
          k = i
          break
        else:
          pass
      lst = [x[:k], x[k:]]
      pig_latin_lst.append(lst[1]+lst[0]+"ay")
  return ' '.join(x for x in pig_latin_lst)
#This is a very long and inefficient cod
#But it's my first time solving a hard question

