
def filter_vowel(s):
  result =''
  for i in s:
    result += i if i in 'aeiou' and i not in result else ''
  return sorted (result)
​
def same_vowel_group(w):  
  temp = filter_vowel(w[0])
  return list(filter(lambda x: filter_vowel(x)==temp,w))

