
def sort_by_letter(lst):
  if lst == []:
    return []
    
  letters = {}
  result = []
  for word in lst:
    for letter in word:
      if letter.isalpha():
        letters[letter] = word
  
  for key in sorted(list(letters.keys())):
    result.append(letters[key])
  
  return result

