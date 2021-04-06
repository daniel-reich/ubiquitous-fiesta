
def duplicate_count(txt):
  count = {}
  for char in txt:
    count[char] = count.get(char, 0) + 1
  return len([char for char, num in count.items() if num > 1])

