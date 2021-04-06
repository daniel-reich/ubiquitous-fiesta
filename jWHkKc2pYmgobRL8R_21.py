
vowels = "a e i o u".split()
​
def distance_to_nearest_vowel(txt):
​
  
  list = []
  
  for idx, l in enumerate(txt):
  
    if l in vowels:
      list.append(0)
    else:
      forward = txt[idx+1:]
      backward = txt[0:idx][::-1]
      #forward = txt[idx+1:]
      #backward = txt[0:idx][::-1]
      
      f_first = first_vowel(forward)
      b_first = first_vowel(backward)
      
      list.append(min(f_first,b_first)+1)
    
  return list
​
def first_vowel(word):
  for i, l in enumerate(word):
    if l in vowels:
      return i
      
  return 1000000

