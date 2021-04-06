
def remove_vowels(string):
  vowels = "aeiouAEIOU"
  answer = ""
  for char in string:
    if char not in vowels:
      answer += char
  return answer

