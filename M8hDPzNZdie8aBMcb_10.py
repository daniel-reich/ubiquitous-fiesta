
def count_substring(s):
  count = 0
  for idx, i in enumerate(s):
    if i == "A":
      count += s[idx:].count("X")
  return count

