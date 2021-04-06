
def average_index(letters):
  total = 0
  for letter in letters:
    total += ord(letter) % 96
  average = total / len(letters)
  return round(average, 2)

