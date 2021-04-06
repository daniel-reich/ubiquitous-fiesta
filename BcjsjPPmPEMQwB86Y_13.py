
def get_vowel_substrings(txt):
  return substrings (txt,"aeiou")
​
def get_consonant_substrings(txt):
  return substrings (txt,"bcdfghjklmnpqrstvwxyz")
  
def substrings (txt,letters):
  fin = []
  for i in range(0,len(txt)):
    if txt[i] in letters:
      for j in range(i,len(txt)):
        if txt[j] in letters:
          if txt[i:j+1] not in fin: fin.append(txt[i:j+1])
  return sorted(fin)

