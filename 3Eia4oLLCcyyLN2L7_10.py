
def remove_repeats(s):
  result = [s[0]]
  for letter in s[1:]:
    if result[-1] != letter:
      result.append(letter)
  return ''.join(result)

