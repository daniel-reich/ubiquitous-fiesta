
def subs(t,x):
  y = sorted([t[i:j+1] for i in x for j in x if i<=j])
  for i in y:
    if y.count(i) > 1:
      y.remove(i)
  return y
​
def get_vowel_substrings(t):
  v = [i for i in range (len(t)) if t[i] in "aeiou"]
  return subs(t,v)
  
def get_consonant_substrings(t):
  c = [i for i in range (len(t)) if t[i] not in "aeiou"]
  return subs(t,c)

