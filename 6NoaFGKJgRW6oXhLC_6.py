
def sum_of_vowels(sentence):
    sentence = sentence.lower()
    count = 0
    
    for ltr in sentence:
      if ltr == 'a':
        count += 4
      elif ltr == 'e':
        count += 3
      elif ltr == 'i':
        count += 1
    
    return count

