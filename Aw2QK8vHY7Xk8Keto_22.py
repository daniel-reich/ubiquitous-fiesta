
def longest_word(s):
  words = s.split(" ")
  longest = words[0]
  for i in words:
    if len(i) > len(longest):
      longest = i
  return longest

