
def is_vowel(l8r):
  vowels = 'aeiou' + 'AEIOU'
  return l8r in vowels
​
def get_vowel_substrings(txt):
  groups = []
​
  for n in range(len(txt)):
    l8r = txt[n]
    if is_vowel(l8r) == True:
      groups.append(l8r)
      for num in range(n+1, len(txt)):
        tl8r = txt[num]
        if is_vowel(tl8r) == True:
          groups.append(txt[n:num+1])
  
  return sorted(list(set(groups)))
​
def get_consonant_substrings(txt):
  groups = []
​
  for n in range(len(txt)):
    l8r = txt[n]
    if is_vowel(l8r) == False:
      groups.append(l8r)
      for num in range(n+1, len(txt)):
        tl8r = txt[num]
        if is_vowel(tl8r) == False:
          groups.append(txt[n:num+1])
  
  return sorted(list(set(groups)))

