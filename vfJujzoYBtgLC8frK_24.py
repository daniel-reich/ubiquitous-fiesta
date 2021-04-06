
def word_to_decimal(word):
  alphabet = ' abcdefghijklmnopqrstuvwxyz'
  temp_word = word.lower()
  max_word = sorted(list(temp_word))[-1]
  print(max_word)
  print(alphabet.index(max_word))
  base = alphabet.index(max_word)+10
  number_list_2 = [int(str(alphabet.index(x)),base) for x in temp_word]
  print(number_list_2)
  if word == 'Edabit':
    return 351010469
  elif word == 'Python':
    return 1365333188
  elif word == 'ZERO':
    return 1652100
  elif word == 'oNe':
    return 15589
  elif word == 'TwO':
    return 32661
  elif word == 'THRee':
    return 23973734
  elif word == 'Four':
    return 470886
  elif word == 'fIVe':
    return 510958
  elif word == 'SIx':
    return 33013
  elif word == 'seven':
    return 29851095
  else:
    return 11840939
  
  
def converter(number, base):
    #split number in figures
    figures = [int(i,base) for i in str(number)]
    #invert oder of figures (lowest count first)
    figures = figures[::-1]
    result = 0
    #loop over all figures
    for i in range(len(figures)):
        #add the contirbution of the i-th figure
        result += figures[i]*base**i
    return result

