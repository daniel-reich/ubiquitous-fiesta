
def most_frequent_char(lst):
  char_dict = {}
  for word in lst:
    for char in word:
      if char in char_dict:
        char_dict[char] += 1
      else:
        char_dict[char] = 1
  max_value = max(char_dict.values())
  max_keys = []
  for key, value in char_dict.items():
    if value == max_value:
      max_keys.append(key)
  return sorted(max_keys)

