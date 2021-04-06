
def pig_latin(txt):
    Vowel = ('A','E','I','O','U','a','i','o','u','e')
    special_character = ('?',"!",".")
    text_dict = txt.split()
    new_dict = []
    for word in text_dict:
      if word[0] in Vowel and word[-1] not in special_character:
        new_dict.append(word + "Way")
      elif word[0] not in Vowel and word[-1] not in special_character:
        new_dict.append(word[1:] + word[0] + 'ay')
      elif word[0] not in Vowel and word[-1] in special_character:
        new_dict.append(word[1:-1] + word[0] + 'ay'+ word[-1])
      else:
        new_dict.append(word[:-1] + "Way"+ word[-1])
    a = (' '.join(new_dict))
    return a.lower().capitalize()

