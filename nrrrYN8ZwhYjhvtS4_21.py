
def extend_vowels(word, num):
  if type(num) == float or num < 0:
    return "invalid"
  result = ""
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  for char in word:
    if char in vowels:
      result += (char*(num+1))
    else:
      result += char
  return result

