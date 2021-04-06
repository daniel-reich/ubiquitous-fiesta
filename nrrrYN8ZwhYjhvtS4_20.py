
def extend_vowels(word, num):
  vowels = "aeiou"
  if num < 0 or type(num) != int:
    return "invalid"
  result = ""
  for letter in word:
    if letter.lower() in vowels:
      result += letter * num
    result += letter
  return result

