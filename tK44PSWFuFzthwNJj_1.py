
def club_entry(word):
  seen = set()
  for letter in word:
    if letter in seen:
      return 4 * (ord(letter) - 96)
    seen.add(letter)

