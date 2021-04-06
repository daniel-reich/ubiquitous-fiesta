
def max_occur(text):
  occur = dict()
  for letter in text:
    if not letter in occur:
      occur[letter] = 1
    else:
      occur[letter] += 1
  max_occur = max(list(occur.values()))
  if max_occur == 1:
    return "No Repetition"
  most = [key for key in occur if occur[key] == max_occur]
  return sorted(most)

