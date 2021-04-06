
def count_vowels(txt):
  vowels = ['a','e','i','o','u']
  return len([char for char in list(txt) if char in vowels])

