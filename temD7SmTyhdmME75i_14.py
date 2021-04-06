
def to_boolean_list(word):
  bitstring_list = convert_to_bitstring(word)
  newlist = []
  for eachpart in bitstring_list:
    if eachpart == 1:
      newlist.append(True)
    else:
      newlist.append(False)
  return newlist
  
  
def convert_to_bitstring(word):
  word = word.lower()
  alphabet = ' abcdefghijklmnopqrstuvwxyz'
  newlist = []
  for eachletter in word:
    if alphabet.index(eachletter) % 2 != 0:
      newlist.append(1)
    else:
      newlist.append(0)
  return newlist

