
def func(txt,vowel:bool):  # txt for text; set vowel=True for get_vowel / False otherwise 
  out=[]
  print(txt)
  for x in range(0,len(txt)):
    if (txt[x] in ['a','e','i','o','u']) == vowel:
#     print(x,":",txt[x])
      for y in range(x,len(txt)):
#       print(x,y,txt[x:y+1])
        if (txt[y] in ['a','e','i','o','u']) == vowel:
          out.append(txt[x:y+1])
  out=list(set(out))   # transform to set to be unique
  out.sort()
  return(out)
​
def get_vowel_substrings(txt):
  return(func(txt,True))
​
def get_consonant_substrings(txt):
  return(func(txt,False))

