
def longest_7segment_word(lst):
  invalid_letters = "kmvwxKMVWX"
  longest = ""
  
  for word in lst:
    if any( c in invalid_letters for c in word ): continue
    if len(word) > len(longest): longest = word
  
  return longest

