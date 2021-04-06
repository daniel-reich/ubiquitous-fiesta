
def rotated_words(txt):
  letters = "HINOXZSMW"
  words = txt.split()
  count = 0
  seen = set()
  for word in words:
    if word in seen:
      continue
    for letter in word:
      if not letter in letters:
        break
    else:
      count += 1
    seen.add(word)
  return count

