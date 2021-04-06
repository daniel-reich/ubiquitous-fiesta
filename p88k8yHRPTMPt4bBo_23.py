
def count_vowels(txt):
  vowels = ["a", "e", "i", "o", "u"]
  count = 0
  for let in txt:
    if let.lower() in vowels:
      count += 1
  return count

